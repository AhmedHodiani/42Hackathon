# ChatBot
This is a chatbot that uses the DistillGPT2 model to generate responses to user queries. It uses the HuggingFace transformers library to load the model and generate responses.

# How it works
Flask is a web framework that allows you to create web applications in Python. It is a simple and easy-to-use framework that allows you to create web applications in a few lines of code.

The chatbot uses Flask to create a web server that listens for requests from the user. When a request is made, the chatbot generates a response to the user's query and returns it in the response body.

We build 3 endpoints:
- /ask
- /messages
- /clear

The frontend is built using HTML, CSS, and JavaScript.



=======================

create venv
```bash
$ python3 -m venv .venv
```


enter the venv
```bash
$ source .venv/bin/activate
```

download the libs
```bash
$ pip install -r requirements.txt
```

start the flask server
```bash
$ python app.py
```
