import nltk


class StopWordsDictionary:

    stopwords_dict = None
    stopwords_replace = None

    @staticmethod
    def load():
        StopWordsDictionary.stopwords_dict = nltk.corpus.stopwords.words('english')
        StopWordsDictionary.stopwords_replace = ''
