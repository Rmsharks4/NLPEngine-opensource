import nltk
from preprocessing.utils.UtilsFactory import UtilsFactory


class WordnetLemmatizer(UtilsFactory):

    lemmatizer_lib = None
    lemmatize_mode = None

    @staticmethod
    def load():
        WordnetLemmatizer.lemmatizer_lib = nltk.stem.WordNetLemmatizer()
        WordnetLemmatizer.lemmatize_mode = 'v'
