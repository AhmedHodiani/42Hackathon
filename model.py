# from transformers import pipeline

# pipe = pipeline("text-generation", model="distilbert/distilgpt2")

# def generate_answer(messages):
#     res = pipe(messages)

#     return (res[0]["generated_text"][-1]['content'])



import torch
from sentence_transformers import SentenceTransformer, util

with open('rag_data.txt', 'r', encoding='utf-8') as file:
    rag_data = file.read().splitlines()

embedder = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedder.encode(rag_data, convert_to_tensor=True)

def retrieve_context(query, top_k=1):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, doc_embeddings, top_k=top_k)
    top_doc = rag_data[hits[0][0]['corpus_id']]
    return top_doc



from transformers import pipeline
pipe = pipeline("text-generation", model="distilbert/distilgpt2")
   
def generate_answer(context, question):
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    result = pipe(prompt, max_new_tokens=30, do_sample=False, temperature=0.5)
    text = result[0]['generated_text']

    answer = text.split("Answer:")[1].split("Question:")[0].strip()
    return answer