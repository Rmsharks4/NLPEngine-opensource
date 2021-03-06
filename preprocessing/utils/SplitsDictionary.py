"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Splits Dictionary**:
reads splits regex from file

"""

from preprocessing.utils.AbstractUtils import AbstractUtils
import re


class SplitsDictionary(AbstractUtils):

    splits_dict = None
    splits_re = None

    @staticmethod
    def load():
        """
        initializes static function load for Splits Dict Class
        """
        SplitsDictionary.splits_dict = {
            '-': ' ',
            '_': ' '
        }
        # '\'s' -> ''
        SplitsDictionary.splits_re = re.compile(r'\b(%s)\b' % '|'.join(SplitsDictionary.splits_dict.keys()))
