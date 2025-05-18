from flask import Flask, request, jsonify
from model import generate_answer
from sql import init_db, insert_message, get_latest_messages
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SYSTEM_PROMPT = """
you are a helpful assistant. you're responses should be short and to the point.
you will be provided the last 5 messages between the user and the assistant.
if the new question is a continuation of the conversation use the previous messages. to know the context.
                        
The last message is the new question
"""

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    if not question or question.strip() == '':
        return jsonify({'error': 'No question provided'})

    print(question)

    messages = get_latest_messages(5)
    messages.insert(0, {"role": "system", "content": SYSTEM_PROMPT})
    messages.append({"role": "user", "content": question})

    print(messages)

    answer = generate_answer(messages)
    insert_message("user", question)
    insert_message("assistant", answer)

    return jsonify({'answer': answer})


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = get_latest_messages(10)
    return jsonify(messages)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
