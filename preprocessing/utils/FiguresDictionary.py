"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Figures Dictionary**:
reads numbers, digits and days from file

"""

import csv
import re
from preprocessing.utils.AbstractUtils import AbstractUtils


class FiguresDictionary(AbstractUtils):

    figures_dict = None
    figures_re = None
    numbers_re = None
    replace_text = None

    @staticmethod
    def load():
        """
        initializes static function load for Figures Dict Class
        """
        with open('../data/Figures_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            FiguresDictionary.figures_dict = dict((rows[0], '#') for rows in reader)
        FiguresDictionary.figures_re = re.compile(r'\b(%s)\b' % '|'.join(FiguresDictionary.figures_dict.keys()))
        FiguresDictionary.numbers_re = re.compile(r'\w*\d\w*')
        FiguresDictionary.replace_text = 'NUMBER'
