import string


class PunctuationDictionary:

    punctuation_dict = None
    punctuation_replace = None

    @staticmethod
    def load():
        PunctuationDictionary.punctuation_dict = string.punctuation
        PunctuationDictionary.punctuation_replace = ''
