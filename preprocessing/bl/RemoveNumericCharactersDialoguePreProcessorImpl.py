
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import re
import csv

with open('../data/Figures_Dict.csv', mode='r') as infile:
    reader = csv.reader(infile)
    figures_dict = dict((rows[0], '#') for rows in reader)
figures_re = re.compile(r'\b(%s)\b' % '|'.join(figures_dict.keys()))


class RemoveNumericCharactersDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def replace(cls, match):
        return figures_dict[match.group(0)]

    @classmethod
    def remove_numeric_characters(cls, text):
        text = re.sub(r'\w*\d\w*', '#', text)
        return figures_re.sub(RemoveNumericCharactersDialoguePreProcessorImpl.replace, text)

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveNumericCharactersDialoguePreProcessorImpl.remove_numeric_characters(text) for text in args]