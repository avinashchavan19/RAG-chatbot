from flask import Flask, request, jsonify
from rag_pipeline import process_document, ask_question

import os

app = Flask(__name__)

UPLOAD_FOLDER = "../uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Upload API
@app.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(file_path)

    result = process_document(file_path)

    return jsonify({
        "message": result
    })


# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Question is required"
        }), 400

    response = ask_question(question)

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)