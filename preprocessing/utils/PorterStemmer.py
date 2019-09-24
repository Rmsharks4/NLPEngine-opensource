"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Porter Stemmer**:
downloads stemmer from nltk

"""

import nltk
from preprocessing.utils.UtilsFactory import UtilsFactory


class PorterStemmer(UtilsFactory):

    stemmer_lib = None

    @staticmethod
    def load():
        PorterStemmer.stemmer_lib = nltk.PorterStemmer()
