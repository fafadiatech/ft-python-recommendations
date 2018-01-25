"""
collaborative has classes to common datasets that have been used for
collaborative filtering
"""
import os
import pandas as pd
from datasets.base import Dataset

class ML100K(Dataset):
    """
    ML100K is Movie Lens 100K Dataset
    More information: https://grouplens.org/datasets/movielens/100k/

    More information can be found in README of the dataset

    Key files in this dataset:

    1. u.item - Contains information about Movies that got rated
                fields include (id, movie name, date of release, IMDB link etc)
                note columns also contains genre information for movies
    2. u.data - Contains rating information from different users
                fields include (user id, item id, rating, timestamp)
    3. u.user - Contains metadata about the users themselves
                fields include (user id, age, gender, occupation, zipcode)

    Note both of these file contain data set in form of:
    (user id, item id, rating, timestamp)

    4. uX.base - The dataset also comes into 5 "folds" this contains 80% of that
    5. uX.test - Contains 20% of remaining fold that will be used for testing
    """
    _ratings = None
    _train_ratings = None
    _test_ratings = None

    # What mode are we initializing the dataset to
    _mode = None

    def __init__(self, mode="test"):
        self._name = "Movie Lens 100K"
        self._download_url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
        self.download_and_unzip()
        self.download_post_process()
        self._mode = mode

    def _load_ratings_file(self, file_path):
        """
        _load_ratings_file is used to load file, this returns a
        pandas DataFrame
        """
        return pd.read_csv(file_path, sep="\t", header=None)

    def download_post_process(self):
        """
        download_post_process is used to read all the datasets

        when in "test" mode, we will load first fold into
        _train_ratings and _test_ratings datasets respectively
        """

        # Load all ratings if we're not testing the algorithm
        if self._mode != "test":
            ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "u.data")
            self._ratings = self._load_ratings_file(ratings_file_path)
        else:
            training_ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "ua.base")
            self._train_ratings = self._load_ratings_file(training_ratings_file_path)

            test_ratings_file_path = os.path.join(self._parent_dir(), "ml-100k", "ua.test")
            self._test_ratings = self._load_ratings_file(test_ratings_file_path)

    def total_instances(self):
        if self._mode != "test":
            return len(self._ratings)
        else:
            return len(self._train_ratings.index), len(self._test_ratings.index)

    def train_test_instance_counts(self):
        """
        train_test_instance_counts is used to get count of training
        and test instances
        """
        return len(self._train_ratings), len(self._test_raings)
