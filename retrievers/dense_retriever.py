from datasetloader import load_scifact
from sentence_transformers import SentenceTransformer
import faiss
import json


def retrieve_text(corpus):
    text_doc = []
    for key, doc in corpus.items():
        text_doc.append(doc["text"])

    return text_doc

def run_dense_retriever(corpus, queries):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    dense_vector = model.encode(retrieve_text(corpus), convert_to_numpy=True, show_progress_bar=True)

    faiss.normalize_L2(dense_vector)
    index = faiss.IndexFlatIP(dense_vector.shape[1])
    index.add(dense_vector)

    doc_ids = list(corpus.keys())

    query_texts = list(queries.values())
    query_vectors = model.encode(query_texts, convert_to_numpy=True, show_progress_bar=True)
    faiss.normalize_L2(query_vectors)

    distances, indices = index.search(query_vectors, 100)

    results = {}
    for i, query_id in enumerate(queries.keys()):
        results[query_id] = {doc_ids[j]: float(distances[i][k]) for k, j in enumerate(indices[i])}
        
    return results
