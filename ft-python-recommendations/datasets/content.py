"""
content has classes to common datasets that have been used for
content based recommendations
"""
import os
import pandas as pd

from datasets.base import Dataset


class NewsDataset(Dataset):
    """
    NewsDataset contains dataset from UCI
    """
    def __init__(self, max_sample=0):
        self._name = "UCI News Dataset"
        self._download_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip"
        self.download_and_unzip()
        self.download_post_process(max_sample)

    def download_post_process(self, max_sample=0):
        """
        once the file has been downloaded do the following:

        1. uncompress the file
        """
        csv_file = os.path.join(self._parent_dir(), "newsCorpora.csv")
        print("Processing:", csv_file)

        if max_sample == 0:
            self.dataset = pd.read_csv(csv_file, sep="\t")
        else:
            self.dataset = pd.read_csv(csv_file, sep="\t", nrows=max_sample)
        self.dataset.columns = ['id', 'content', 'url;', 'publisher',
                                'category', 'story', 'hostname', 'timestamp']
        print("Loaded dataset")

    def total_instances(self):
        return len(self.dataset)
