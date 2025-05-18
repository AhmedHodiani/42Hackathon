from flask import Flask, request, jsonify
from model import generate_answer
from sql import init_db, insert_message, get_latest_messages

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    print(question)


    messages = get_latest_messages(10)
    messages.insert(0, {"role": "system", "content": "you are a helpful assistant."})
    messages.append({"role": "user", "content": question})

    print(messages)

    answer = generate_answer(messages)
    insert_message("user", question)
    insert_message("assistant", answer)

    return jsonify({'answer': answer})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
