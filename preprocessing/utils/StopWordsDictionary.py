"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Stop Words Dictionary**:
downloads stop words from nltk

"""

import nltk
from preprocessing.utils.UtilsFactory import UtilsFactory


class StopWordsDictionary(UtilsFactory):

    stopwords_dict = None
    stopwords_replace = None

    @staticmethod
    def load():
        StopWordsDictionary.stopwords_dict = nltk.corpus.stopwords.words('english')
        StopWordsDictionary.stopwords_replace = ''
