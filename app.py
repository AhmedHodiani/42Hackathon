from flask import Flask, request, jsonify
from model import generate_answer

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    print(question)

    messages = [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": question},
    ]

    return jsonify({'answer': generate_answer(messages)})

if __name__ == '__main__':
    app.run(debug=True)
