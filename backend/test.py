from rag_pipeline import process_document, ask_question

# Process document
process_document("../uploads/test.txt")

# Ask question
response = ask_question("What is AI?")

print(response)