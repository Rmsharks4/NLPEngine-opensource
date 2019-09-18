import csv
import re


class FiguresDictionary:

    figures_dict = None
    figures_re = None
    numbers_re = None
    replace_text = None

    @staticmethod
    def load():
        with open('../data/Figures_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            FiguresDictionary.figures_dict = dict((rows[0], '#') for rows in reader)
        FiguresDictionary.figures_re = re.compile(r'\b(%s)\b' % '|'.join(FiguresDictionary.figures_dict.keys()))
        FiguresDictionary.numbers_re = re.compile(r'\w*\d\w*')
        FiguresDictionary.replace_text = '$NUMBER'
