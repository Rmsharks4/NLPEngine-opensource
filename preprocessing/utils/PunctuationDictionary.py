"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Punctuation Dictionary**:
downloads punctuation dict from nltk

"""

import string
from preprocessing.utils.AbstractUtils import AbstractUtils


class PunctuationDictionary(AbstractUtils):

    punctuation_dict = None
    punctuation_replace = None

    @staticmethod
    def load():
        """
        initializes static function load for Punctuations Dict Class
        """
        PunctuationDictionary.punctuation_dict = string.punctuation
        PunctuationDictionary.punctuation_replace = ''
