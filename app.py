import os
import docx
import fitz
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shivam-bot'
CORS(app)

# Load a pre-trained question-answering model from Hugging Face Transformers
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", tokenizer="distilbert-base-cased-distilled-squad")

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    # Use the question-answering model to find the answer in the given documents
    answer = get_answer_from_documents(user_message)

    if answer:
        response_message = answer
    else:
        response_message = "I don't know the answer to this."

    return jsonify({'message': response_message})


def get_answer_from_documents(question):

    # Replace this with the actual path to your document folder
    document_folder = "./documents"

    # Read through the documents in the specified folder
    document_texts = []

    for filename in os.listdir(document_folder):
        file_path = os.path.join(document_folder, filename)

        # Check if the file is a Word or PDF document
        if filename.lower().endswith(".docx"):
            document_texts.append(read_docx(file_path))
        elif filename.lower().endswith(".pdf"):
            document_texts.append(read_pdf(file_path))

    # Concatenate the document texts into a single string
    documents_text = " ".join(document_texts)

    # Use the question-answering model to find the answer
    answer = qa_model(question=question, context=documents_text)

    return answer['answer']

def read_docx(file_path):
    # docx library is used to extract text from Word documents
    doc = docx.Document(file_path)

    # Extract the text from each paragraph
    paragraphs = [paragraph.text for paragraph in doc.paragraphs]
    return " ".join(paragraphs)

def read_pdf(file_path):
    # PyMuPDF (MuPDF) library is used to extract text from PDF
    doc = fitz.open(file_path)
    text = ""

    # Extract the text from each page
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    return text

if __name__ == '__main__':
    app.run(debug=True)
