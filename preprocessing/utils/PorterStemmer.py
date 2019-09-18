import nltk


class PorterStemmer:

    stemmer_lib = None

    @staticmethod
    def load():
        PorterStemmer.stemmer_lib = nltk.PorterStemmer()
