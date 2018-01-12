import string
from collections import defaultdict
from config import settings


class TextTransform:
    """
    TextTransform is a collection of function that are used to cleanup text
    """
    _stopwords = None

    def __init__(self):
        """
        do some initialization

        e.g. read stoplist
        """
        results = []
        with open(settings.STOPLIST_FILE_PATH) as stoplist:
            for token in stoplist.readlines():
                results.append(token.strip())

        # We want to convert this to set
        # because lookups in sets are a bit faster
        self._stopwords = set(results)

    def strip_punctuations(self, snippet):
        """
        strip_punctuations is used to get rid of all the punctuations
        """
        exclude = set(string.punctuation)
        return ''.join(ch for ch in snippet if ch not in exclude)

    def cleanup(self, snippet):
        """
        clenup is used to get rid of all words that are stoplist,
        it also does lower case transformation
        """
        is_not_stopword = lambda token: token not in self._stopwords
        results = []

        tokens = self.strip_punctuations(snippet.lower()).split()
        for token in tokens:
            if is_not_stopword(token):
                results.append(token)

        return " ".join(results)

    def vectorize_by_counts(self, snippet):
        """
        vectorize_by_counts is function given a snippet it will
        return a dictionary of token an count
        """
        result = defaultdict(int)

        for token in self.cleanup(snippet).split():
            result[token] += 1

        return result
