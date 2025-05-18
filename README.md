understand the tools of running the model
- making a python venv (10 min)
- installing the libs (5 min)
- understading the libs (1-2 hour)
- downloading the model (30 min)
- running the model (2 hour)
     - tokens
     - print
     - take input


flask!! (backend) (20 min)
- build our first API /ask (request and respones)
(1:30 min)


(5 hour)
-RAG and History System


(2 hour)
-frontend



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

=======================

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you?"},
]

def build_prompt(messages):
    prompt = ""
    for msg in messages:
        role_tag = msg["role"]
        content = msg["content"]
        prompt += f"<|{role_tag}|>\n{content}\n"
    prompt += "<|assistant|>\n"
    return prompt

prompt = build_prompt(messages)
inputs = tokenizer(prompt, return_tensors="pt")

input_length = inputs.input_ids.shape[-1]

outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
)

generated_tokens = outputs[0][input_length:]
print(tokenizer.decode(generated_tokens, skip_special_tokens=True))
```



or with the pipeline

```python
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Who are you?"},
]
res = pipe(messages)


print(res[0]["generated_text"][-1]['content'])
```
