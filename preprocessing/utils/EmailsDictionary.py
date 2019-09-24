"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Emails Dictionary**:
reads email regex from file

"""

import re
from preprocessing.utils.UtilsFactory import UtilsFactory


class EmailsDictionary(UtilsFactory):

    standard_re = None
    semi_standard_re = None
    non_standard_re = None
    replace_text = None

    @staticmethod
    def load():
        EmailsDictionary.standard_re = re.compile(r'\w*@\w*\.\w*')
        EmailsDictionary.semi_standard_re = re.compile(r'\w*\.\w*')
        EmailsDictionary.non_standard_re = re.compile(r'\w*\sdot\s\w*')
        EmailsDictionary.replace_text = '$EMAIL'
