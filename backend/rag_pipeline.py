from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

VECTOR_DB_PATH = "../vectorstore"

# Create embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def process_document(file_path):

    # Detect file type
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)

    else:
        return "Unsupported file format"

    # Load document
    documents = loader.load()

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    # Create vectorstore
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Save vectorstore
    vectorstore.save_local(VECTOR_DB_PATH)

    return "Document processed successfully"


def ask_question(question):

    # Load vector database
    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Similarity search
    results = vectorstore.similarity_search(question, k=2)

    answer = ""

    sources = []

    for doc in results:
        answer += doc.page_content + "\n"
        sources.append(doc.metadata)

    return {
        "answer": answer,
        "sources": sources
    }