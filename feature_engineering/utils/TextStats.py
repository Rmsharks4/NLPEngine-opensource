from textstat.textstat import textstatistics, easy_word_set
from feature_engineering.utils.AbstractUtils import AbstractUtils


class TextStats(AbstractUtils):

    ts = None
    es = None

    @staticmethod
    def load():
        TextStats.ts = textstatistics()
        TextStats.es = easy_word_set
