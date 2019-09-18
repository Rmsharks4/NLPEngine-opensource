
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
import re
import csv


class RemoveNumericCharactersDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = ExpandContractionsDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None
        with open('../data/Figures_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.figures_dict = dict((rows[0], '#') for rows in reader)
        self.figures_re = re.compile(r'\b(%s)\b' % '|'.join(self.figures_dict.keys()))

    @classmethod
    def replace(cls, match):
        return cls.figures_dict[match.group(0)]

    @classmethod
    def remove_numeric_characters(cls, text):
        text = re.sub(r'\w*\d\w*', '#', text)
        return cls.figures_re.sub(RemoveNumericCharactersDialoguePreProcessorImpl.replace, text)

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveNumericCharactersDialoguePreProcessorImpl.remove_numeric_characters(text) for text in args]