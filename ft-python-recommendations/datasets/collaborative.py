"""
collaborative has classes to common datasets that have been used for
collaborative filtering
"""
import os
from datasets.base import Dataset

class ML100K(Dataset):
    """
    ML100K is Movie Lens 100K Dataset
    More information: https://grouplens.org/datasets/movielens/100k/
    """
    _ratings = []
    _train_ratings = []
    _test_raings = []

    def __init__(self):
        self._name = "Movie Lens 100K"
        self._download_url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
        self.download_and_unzip()

    def _load_ratings_file(self, file_path):
        """
        _load_ratings_file is used to load file
        """
        results = []
        with open(file_path) as ratings:
            for row in ratings.readlines():
                row = row.strip()
                results.append(row.split("\t"))
        return results

    def download_post_process(self):
        """
        download_post_process is used to read all the datasets
        """
        ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "u.data")
        self._ratings = self._load_ratings_file(ratings_file_path)

        ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "u.data")
        self._ratings = self._load_ratings_file(ratings_file_path)

        training_ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "ua.base")
        self._train_ratings = self._load_ratings_file(training_ratings_file_path)

        test_ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "ua.test")
        self._test_raings = self._load_ratings_file(test_ratings_file_path)

    def total_instances(self):
        return len(self._ratings)
    
    def train_test_instance_counts(self):
        """
        train_test_instance_counts is used to get count of training
        and test instances
        """
        return len(self._train_ratings), len(self._test_raings)
