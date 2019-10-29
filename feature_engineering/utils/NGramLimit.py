
from feature_engineering.utils.AbstractUtils import AbstractUtils


class NGramLimit(AbstractUtils):

    ngram = None

    @staticmethod
    def load():
        NGramLimit.ngram = 3
