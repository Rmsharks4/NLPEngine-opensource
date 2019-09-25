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
from preprocessing.utils.AbstractUtils import AbstractUtils


class ContractionsDictionary(AbstractUtils):

    contractions_dict = None
    contractions_re = None

    @staticmethod
    def load():
        """
        initializes static function load for Contractions Dict Class
        """
        with open('../data/Contractions_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            ContractionsDictionary.contractions_dict = dict((rows[0], rows[1]) for rows in reader)
        ContractionsDictionary.contractions_re = re.compile('(%s)' % '|'.join(ContractionsDictionary.contractions_dict.keys()))
