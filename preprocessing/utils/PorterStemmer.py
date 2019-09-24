import nltk
from preprocessing.utils.UtilsFactory import UtilsFactory


class PorterStemmer(UtilsFactory):

    stemmer_lib = None

    @staticmethod
    def load():
        PorterStemmer.stemmer_lib = nltk.PorterStemmer()
