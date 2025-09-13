import json
from datasetloader import load_scifact
from retrievers.dense_retriever import run_dense_retriever
from retrievers.sparse_retriever import run_sparse_retriever

if __name__ == "__main__":
    corpus, queries, _ = load_scifact(split="test")

    print("Running sparse retriever")
    sparse_results = run_sparse_retriever(corpus, queries)
    with open("results/sparse_results.json", "w", encoding="utf-8") as f:
        json.dump(sparse_results, f, ensure_ascii=False, indent=2)

    print("Retrrievals completed for sparse retriever")

    print("Running dense retriever")
    dense_results = run_dense_retriever(corpus, queries)
    with open("results/dense_results.json", "w", encoding="utf-8") as f:
        json.dump(dense_results, f, ensure_ascii=False, indent=2)

    print("All retrievals completed successfully!")
