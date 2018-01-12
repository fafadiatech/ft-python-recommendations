import os
import pandas as pd

from datasets.base import Dataset


class NewsDataset(Dataset):
    """
    NewsDataset contains dataset from UCI
    """
    def __init__(self):
        self._name = "UCI News Dataset"
        self._download_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip"

    def download_post_process(self):
        """
        once the file has been downloaded do the following:

        1. uncompress the file
        """
        csv_file = os.path.join(self._parent_dir(), "newsCorpora.csv")
        print("Processing:", csv_file)

        self.dataset = pd.read_csv(csv_file, sep="\t")
        self.dataset.columns = ['id', 'title', 'url;', 'publisher',
                           'category', 'story', 'hostname', 'timestamp']
        print("Loaded dataset")
        print(self.dataset.head())
        print(len(self.dataset))

    def total_instances(self):
        return len(self.dataset)
