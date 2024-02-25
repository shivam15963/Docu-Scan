from flask import Flask, request, jsonify, session
from flask_cors import CORS
from knowledge_base import knowledge_base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shivam-bot'
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():

    # Get the user's message
    user_message = request.json.get('message', '')

    # If you want to use a knowledge base, you can add it here
    if user_message in knowledge_base:
        response_message = knowledge_base[user_message]
    else:
        response_message = "I don't know the answer to this."

    return jsonify({'message': response_message})

if __name__ == '__main__':
    app.run(debug=True)
