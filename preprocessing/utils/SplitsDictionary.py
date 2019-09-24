"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Splits Dictionary**:
reads splits regex from file

"""

from preprocessing.utils.UtilsFactory import UtilsFactory


class SplitsDictionary(UtilsFactory):

    splits_dict = None
    splits_replace = None

    @staticmethod
    def load():
        SplitsDictionary.splits_dict = ['-', '_']
        SplitsDictionary.splits_replace = ' '
