"""
test_text contains test cases for unittesting TextTansform
classes
"""
from transforms.text import TextTransform


def test_strip_punctuation():
    transform = TextTransform()
    assert transform.strip_punctuations("hello' world") == "hello world"

def test_strip_stopwords():
    transform = TextTransform()
    assert transform.cleanup("This is a test") == "test"

def test_vectorize_by_counts():
    transform = TextTransform()
    exptected = {111: 2, 518: 1}
    actual = transform.vectorize_by_counts("THIS IS A TEST yet test")
    assert len(actual) == len(exptected)
    assert actual[111] == exptected[111]
    assert 518 in actual
