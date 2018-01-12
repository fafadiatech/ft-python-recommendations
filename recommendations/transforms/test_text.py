from transforms.text import TextTransform


def test_strip_punctuation():
    transform = TextTransform()
    assert transform.strip_punctuations("hello' world") == "hello world"

def test_strip_stopwords():
    transform = TextTransform()
    assert transform.cleanup("This is a test") == "test"

def test_vectorize_by_counts():
    transform = TextTransform()
    exptected = {"test": 2, "yet": 1}
    actual = transform.vectorize_by_counts("THIS IS A TEST yet test")
    assert len(actual) == len(exptected)
    assert actual["test"] == exptected["test"]
    assert "yet" in actual
