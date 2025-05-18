from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

with open('rag_data.txt', 'r', encoding='utf-8') as file:
    rag_data = file.read().splitlines()


embedder = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = embedder.encode(rag_data, convert_to_tensor=True)
pipe = pipeline("text-generation", model="distilbert/distilgpt2")



def retrieve_context(query, top_k=1):
    query_embedding = embedder.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, doc_embeddings, top_k=top_k)
    contexts = []

    for hit in hits[0]:
        if hit['score'] > 0.40:
            print("score: ", hit['score'], "context: ", rag_data[hit['corpus_id']])
            contexts.append(rag_data[hit['corpus_id']])
    return contexts


def generate_answer(contexts, question):
    prompt = ""
    for context in contexts:
        qna = context.split('?')
        prompt += f"Question: {qna[0]}\nAnswer: {qna[1]}\n"

    prompt += f"Question: {question}\nAnswer: "
    result = pipe(prompt, do_sample=False, temperature=0.5)
    text = result[0]['generated_text']

    answer = text.split("Answer:")[1].split("Question:")[0].strip()
    return answer