from models.content import CountBased

def test_initialization():
    algorithm = CountBased()
    assert algorithm is not None
