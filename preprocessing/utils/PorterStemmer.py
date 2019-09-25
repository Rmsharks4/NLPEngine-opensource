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
from preprocessing.utils.AbstractUtils import AbstractUtils


class PorterStemmer(AbstractUtils):

    stemmer_lib = None

    @staticmethod
    def load():
        """
        initializes static function load for Porter Stemmer Class
        """
        PorterStemmer.stemmer_lib = nltk.PorterStemmer()
