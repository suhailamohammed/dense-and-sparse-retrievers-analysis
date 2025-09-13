from beir import util
from beir.datasets.data_loader import GenericDataLoader
import os, pathlib

def load_scifact(split):
    data_path = "datasets/scifact"

    if not os.path.exists(data_path):
        print("downloading datasets")
        dataset = "scifact"
        url = f"https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{dataset}.zip"
        out_dir = os.path.join(pathlib.Path(__file__).parent.absolute(), "datasets")
        data_path = util.download_and_unzip(url, out_dir)

    print("loading dataset")
    corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split=split)
    return corpus, queries, qrels