"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Word Net Lemmatizer**:
downloads lemmatizer from nltk

"""

import nltk
from preprocessing.utils.AbstractUtils import AbstractUtils


class WordnetLemmatizer(AbstractUtils):

    lemmatizer_lib = None
    lemmatize_mode = None

    @staticmethod
    def load():
        """
        initializes static function load for Wordnet Lemmatizer Class
        """
        WordnetLemmatizer.lemmatizer_lib = nltk.stem.WordNetLemmatizer()
        WordnetLemmatizer.lemmatize_mode = 'v'
