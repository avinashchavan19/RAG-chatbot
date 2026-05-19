# 🤖 RAG Chatbot (Retrieval-Augmented Generation)

## 📌 Overview
This project is a **RAG (Retrieval-Augmented Generation) Chatbot** that answers user queries based on custom uploaded documents.

---

## 🚀 Features
- Ask questions from your own documents
- Context-based intelligent answers
- Fast semantic search using vector embeddings
- Efficient retrieval using FAISS / vector database
- Simple web interface using Flask
- Backend API for processing queries

---

## 🛠️ Tech Stack
- Python
- Flask
- FAISS / ChromaDB (Vector Database)
- NLP / Embeddings
- HTML, CSS (Frontend)

---

## 🧠 How It Works
- User uploads or provides documents  
- Text is split into smaller chunks  
- Embeddings are generated for each chunk  
- Stored in a vector database (FAISS)  
- User query is converted into embedding  
- Most relevant chunks are retrieved  
- LLM generates final answer using retrieved context  

---

## 📂 Project Structure

Rag_chatbot/
│
├── backend/
├── frontend/
├── uploads/
├── vectorstore/
├── assets/
├── .gitignore
├── README.md
├── requirements.txt

---

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
git clone https://github.com/avinashchavan19/rag-chatbot.git
cd rag-chatbot

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the project
python app.py

## 📸 Screenshots

### 🟢 Initial Interface
![Initial UI](assets/initial.png)

### 🔵 Output Example
![Output UI](assets/output.png)

## 🎯 Future Improvements
Multi-document support
Improved UI/UX
Cloud deployment (Render / AWS / HuggingFace)
Authentication system
Better retrieval accuracy

## 👨‍💻 Author

Avinash Chavan
AI & Data Science Student
GitHub: https://github.com/avinashchavan19
