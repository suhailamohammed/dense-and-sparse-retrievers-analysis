
## Project Overview
This project demonstrates a text retrieval system using different retrievers. It allows you to load a dataset, run retrieval experiments, and compare performance between the sparse and dense retrievers.

## Project Structure
```
project_root/
│
├── datasetloader.py           # Script to load dataset
├── retrievers/                # Implementations of different retrievers
|      └── dense_retriever.py  # Script contains implementation of dense retriever
|      └── sparse_retriever.py # Script contains implementation of sparse retriever
├── results/                   # Folder where retrieval results are saved
├── evaluation.py              # Script for evaluation of retrievers
├── requirements.txt           # Python dependencies
└── main.py                    # Main script to run retrieval
```

## Instructions
Follow these steps to set up the environment and run the code:

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dataset loader and retrieval script**:
   ```bash
   python main.py
   ```
   This will first load the dataset and run both retriever scripts to generate results for the sparse and dense retrievers, then save the outputs in the `results/` folder.

5. **Run the evaluation script**:
   ```bash
   python evaluation.py
   ```
    This will display the evaluation score for both of the retrievers in the terminal output.

## Results Discussion
After running the scripts, the retrievers can be compared using the following information:

- **Which metrics were used for evaluation?**  
    - Normalized Discounted Cumulative Gain (NDCG) - Measures the quality of ranking.
    - Mean Average Precision (MAP) - Measures the average precision across all relevant documents for a query, then averages over all queries.
    - Recall - Measures the fraction of relevant documents retrieved out of all relevant documents available.
    - Precision - Measures the fraction of retrieved documents that are relevant.

    These metrics were used for top 10 and 100 documents.

- **Retrieval Performance Comparison**

    | Metric     | Sparse Retriever @10 | Sparse Retriever @100 | Dense Retriever @10 | Dense Retriever @100 |
    |------------|-------------------|--------------------|-------------------|--------------------|
    | NDCG       | 0.62176           | 0.64755            | 0.6402            | 0.66904            |
    | MAP        | 0.5815            | 0.58715            | 0.58873           | 0.59504            |
    | Recall     | 0.73417           | 0.84722            | 0.78667           | 0.91667            |
    | Precision  | 0.08              | 0.00953            | 0.089             | 0.01047            |


- **Which retriever performed better?**  
  For both retrievers, increasing the number of top-k documents retrieved generally led to higher evaluation scores which indicated that both retrievers perform better when more documents are considered. However, dense retriever scores slightly higher across all metrics (NDCG, MAP, Recall, Precision) for both top-10 and top-100. It has high recall, which indicates that it finds a larger portion of all relevant documents because due to the ability to capture semantic relevance rather than relying solely on keyword matching like the sparse retriever.

- **Performance Trade-offs Observed**:
  - **Speed vs. Quality**: Sparse retriever was faster but less accurate whereas dense retriever was more slower but abit more accurate.  
  - **Memory Usage**: Dense retriever required more memory for embeddings.  
  - **Retrieval Quality**: Sparse methods like BM25 are lightweight but may miss semantic matches.

- **Concluding statement**  
  In my opinion, even though the dense retriever achieved better results, the improvement was not very large. The margin between the two retrievers was small for most metrics. For this dataset, it can be argued that the sparse retriever might be a better choice in terms of memory efficiency and overall performance. Additionally, the dense retriever tends to be more computationally expensive than the sparse retriever.