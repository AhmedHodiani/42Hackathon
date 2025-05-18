from flask import Flask, request, jsonify
from model import generate_answer, retrieve_context
from sql import init_db, insert_message, get_latest_messages, truncate_table
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    if not question or question.strip() == '':
        return jsonify({'error': 'No question provided'})

    print(question)

    contexts = retrieve_context(question, 3)
    print("============: ", contexts)
    answer = generate_answer(contexts, question)
 
    insert_message("user", question)
    insert_message("assistant", answer)

    return jsonify({'answer': answer})


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = get_latest_messages(20)
    return jsonify(messages)


@app.route('/clear', methods=['POST'])
def clear_messages():
    truncate_table()
    return jsonify({'message': 'Messages cleared'})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
