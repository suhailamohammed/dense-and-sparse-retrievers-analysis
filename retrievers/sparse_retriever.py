from rank_bm25 import BM25Okapi
import re

def regex(text):
    return re.sub(r"[^\w\s-]", "", text.lower())

def generate_token_vector(corpus):
    tokenized_vector = {}

    for doc_id, doc in corpus.items():
        text = regex(doc["text"])
        tokenized_vector[doc_id] = text.split(" ")

    return tokenized_vector

def generate_bm25(token_vector):
    list_token_vectors = list(token_vector.values())
    bm25 = BM25Okapi(list_token_vectors)
    return bm25

def top_score_docs(k, query, corpus_keys, bm25):
    query_tokens = regex(query).split(" ")

    scores = bm25.get_scores(query_tokens)
    top_k_indices = scores.argsort()[::-1][:k]

    top_docs = {corpus_keys[i]: round(float(scores[i]), 2) for i in top_k_indices}

    return top_docs

def run_sparse_retriever(corpus, queries):
    token_vector = generate_token_vector(corpus)
    bm25 = generate_bm25(token_vector)
    corpus_keys = list(corpus.keys())

    query_doc = {}
    for id, query in queries.items():
        query_doc[id] = top_score_docs(100, query, corpus_keys, bm25)

    return query_doc
