"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Contractions Dictionary**:
reads a contractions dict and regex from file

"""

import re
import csv
from preprocessing.utils.UtilsFactory import UtilsFactory


class ContractionsDictionary(UtilsFactory):

    contractions_dict = None
    contractions_re = None

    @staticmethod
    def load():
        with open('../data/Contractions_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            ContractionsDictionary.contractions_dict = dict((rows[0], rows[1]) for rows in reader)
        ContractionsDictionary.contractions_re = re.compile('(%s)' % '|'.join(ContractionsDictionary.contractions_dict.keys()))
