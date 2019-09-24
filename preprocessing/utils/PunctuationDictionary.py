import string
from preprocessing.utils.UtilsFactory import UtilsFactory


class PunctuationDictionary(UtilsFactory):

    punctuation_dict = None
    punctuation_replace = None

    @staticmethod
    def load():
        PunctuationDictionary.punctuation_dict = string.punctuation
        PunctuationDictionary.punctuation_replace = ''
