import nltk
from preprocessing.utils.UtilsFactory import UtilsFactory


class StopWordsDictionary(UtilsFactory):

    stopwords_dict = None
    stopwords_replace = None

    @staticmethod
    def load():
        StopWordsDictionary.stopwords_dict = nltk.corpus.stopwords.words('english')
        StopWordsDictionary.stopwords_replace = ''
