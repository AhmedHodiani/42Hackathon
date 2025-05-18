from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

def generate_answer(messages):
    res = pipe(messages)

    return (res[0]["generated_text"][-1]['content'])
