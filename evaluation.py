import json
import sys
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval


def main():
    """
    This script evaluates the performance of a retrieval system.
    It expects two arguments:
    1. The path to the directory containing the dataset (e.g., 'datasets/scifact').
    2. The path to the results file (e.g., 'results/bm25_results.json').
    """
    # if len(sys.argv) != 3:
    #     print("Usage: python evaluation.py <dataset_path> <results_file_path>")
    #     sys.exit(1)

    dataset_path = "datasets/scifact"
    sparse_results_file_path = "results/sparse_results.json"
    dense_results_file_path = "results/dense_results.json"


    # Load the dataset and qrels
    try:
        _, _, qrels = GenericDataLoader(data_folder=dataset_path).load(split="test")
    except Exception as e:
        print(f"Error loading dataset from {dataset_path}: {e}")
        sys.exit(1)

    # Load the results from the retrieval system
    try:
        with open(sparse_results_file_path, "r") as f:
            results_sparse = json.load(f)
        with open(dense_results_file_path, "r") as f:
            results_dense = json.load(f)
    except FileNotFoundError as e:
        print(f"Error: Results file not found. {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode JSON. {e}")
        sys.exit(1)

    # Initialize the evaluator
    evaluator = EvaluateRetrieval()

    # Evaluate the results
    print(f"Evaluating results from {sparse_results_file_path}...")
    scores_sparse = evaluator.evaluate(qrels, results_sparse, [10, 100])
    
    print(f"Evaluating results from {dense_results_file_path}...")
    scores_dense = evaluator.evaluate(qrels, results_dense, [10, 100])



    # Print the scores
    print("\nEvaluation Scores for sparse retriever:")
    print(json.dumps(scores_sparse, indent=4))

    print("\nEvaluation Scores for dense retriever:")
    print(json.dumps(scores_dense, indent=4))

if __name__ == "__main__":
    main()
