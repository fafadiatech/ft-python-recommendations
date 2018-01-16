"""
test_content contains few test cases for unit-testing
content based recommendation algorithm
"""

from models.content import CountBased
from datasets.content import NewsDataset

def test_initialization():
    algorithm = CountBased()
    assert algorithm is not None

def test_jaccard_distance():
    algorithm = CountBased()
    assert algorithm.compute_distance(['1', '2', '3'], ['2', '3']) == 2/3.0

def test_count_based_recommender():
    dataset = NewsDataset(200)
    recommender = CountBased()
    recommender.train(dataset.get_instances())
    actual = recommender.predict(182)
    assert len(actual) == 5
    doc_id, score = actual[0]
    assert doc_id == 177
    assert score == float(1)

def test_save_and_load_disk():
    dataset = NewsDataset(200)
    recommender = CountBased()
    recommender.train(dataset.get_instances())
    recommender.save_to_disk()

    expected_vocab_length = recommender.vocabulary_count()
    recommender.load_from_disk()
    assert recommender.vocabulary_count() == expected_vocab_length
    