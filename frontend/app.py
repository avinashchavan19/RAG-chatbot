import streamlit as st
import requests

st.title("RAG Based Chatbot")

# Upload section
uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "txt"]
)

if uploaded_file is not None:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://127.0.0.1:5000/upload",
        files=files
    )

    st.success(response.json()["message"])


# Chat section
question = st.text_input("Ask a Question")

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:5000/chat",
        json={
            "question": question
        }
    )

    data = response.json()

    st.subheader("Answer")
    st.write(data["answer"])

    st.subheader("Sources")
    st.write(data["sources"])