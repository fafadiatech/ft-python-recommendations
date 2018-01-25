from models.collaborative import ItemToItemAlgorithm
from datasets.collaborative import ML100K

def test_initialization():
    algorithm = ItemToItemAlgorithm()
    assert algorithm is not None