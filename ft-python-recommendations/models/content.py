"""
content module has class impementation of content based recommendations
"""

import os
import pickle
import pathlib
import operator
import itertools

from config import settings
from models.base import RecommendationAlgorithm
from transforms.text import TextTransform

class CountBased(RecommendationAlgorithm):
    """
    CountBased is a simple recommendation algorithm that is based on
    simple counting feature {1-gram}
    """
    _vocabulary = []
    _features = {}
    transform = None

    # This is used to store similarity score between two token_id
    # key is token_id_1:token_id_2 -> value is similarity score
    similarity = {}

    def __init__(self):
        self.transform = TextTransform()

    def _iter_pairs(self):
        """
        _iter_pairs is a generator expression that is used to generate unique pairs
        reason we want to do this is to avoid re-computing commutative score
        E.g.:
        sim(1,2) = sim(2, 1)
        so we simply won't compute sim(2, 1)
        """
        for pair in itertools.combinations(range(1, len(self.transform.vocabulary)), r=2):
            yield pair

    def compute_distance(self, set_a, set_b, metric="jaccard"):
        """
        compute_distance method is used to compute similarity distance

        for now we've implemented jaccard, later on we will implement different
        """

        # make sure to transform list to set
        set_a = set(set_a)
        set_b = set(set_b)
        union_count = len(set_a.union(set_b))
        intersection_count = len(set_a.intersection(set_b))
        if intersection_count > 0:
            return intersection_count / float(union_count)
        return float(0)

    def train(self, dataset, min_sim_score=0.30, top_n=10, metric="jaccard"):
        """
        train method is basically iterating over dataset and compute topK
        similar items

        for dataset we're expecting atleast two columns {id, content}
        """
        # dataset is a pandas data frame, based on this we need to update our internal datastructure
        for i, row in dataset.iterrows():
            doc_id, doc_contents = int(row['id']), row['content']
            self._features[doc_id] = self.transform.vectorize_by_counts(doc_contents)

        print("Completed extracting count features of test instances")

        # Compute pairwise similarities
        for pair in self._iter_pairs():
            doc_a, doc_b = pair
            if doc_a in self._features and doc_b in self._features:
                sim_score = self.compute_distance(
                    self._features[doc_a], self._features[doc_b])
                if sim_score > min_sim_score:
                    key = "%s:%s" % (doc_a, doc_b)
                    self.similarity[key] = sim_score

        print("Completed computing similarities")

    def _store_as_pickle(self, item_to_persist, file_path):
        """
        _store_as_pickle is reusable function to persist objects to disk
        """
        with open(file_path, "wb") as file_to_save:
            pickle.dump(item_to_persist, file_to_save)
        print(f"Completed storing to:{file_path}")

    def _load_as_pickle(self, file_path):
        """
        _load_as_pickle is reusable function to load persist objects from disk
        """
        with open(file_path, "rb") as file_to_load:
            return pickle.load(file_to_load)
        return None

    def save_to_disk(self, dir_to_save_path=None):
        """
        save_to_disk method is used to save

        1. _vocabulary
        2. _features

        to disk, so that they can be retrieved in future
        """
        if dir_to_save_path is None:
            dir_to_save_path = os.path.join(settings.PROJECT_ROOT, "persistence", "count_based")

        # Make sure we have the path created, if it already exists
        # ignore it
        pathlib.Path(dir_to_save_path).mkdir(parents=True, exist_ok=True)

        vocab_disk_path = os.path.join(dir_to_save_path, "vocabulary.pkl")
        self._store_as_pickle(self._vocabulary, vocab_disk_path)

        features_disk_path = os.path.join(dir_to_save_path, "features.pkl")
        self._store_as_pickle(self._features, features_disk_path)

    def load_from_disk(self, dir_to_load_path=None):
        """
        load_from_disk method is used to load files saved using 
        save_to_disk, i.e.

        1. _vocabulary
        2. _features
        """

        if dir_to_load_path is None:
            dir_to_load_path = os.path.join(settings.PROJECT_ROOT, "persistence", "count_based")

        vocab_disk_path = os.path.join(dir_to_load_path, "vocabulary.pkl")
        self._vocabulary = self._load_as_pickle(vocab_disk_path)

        features_disk_path = os.path.join(dir_to_load_path, "features.pkl")
        self._features = self._load_as_pickle(features_disk_path)

    def predict(self, doc_id):
        """
        predict method will return results sorted as list of tuple (doc_id, score)
        """
        results = []

        if doc_id in self._features:
            for pair, score in self.similarity.items():
                item_a, item_b = list(map(int, pair.split(":")))

                if item_a == doc_id:
                    results.append((item_b, score))

                if item_b == doc_id:
                    results.append((item_a, score))

        results.sort(key=operator.itemgetter(1), reverse=True)
        return results

    def vocabulary_count(self):
        """
        vocabulary_count is used to return count of vocabulary
        """
        return len(self._vocabulary)