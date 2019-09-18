
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsPreProcessorImpl
import csv
import re


class ExpandContractionsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = SplitJointWordsPreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None
        with open('../data/Contractions_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            self.contractions_dict = dict((rows[0], rows[1]) for rows in reader)
        self.contractions_re = re.compile('(%s)' % '|'.join(self.contractions_dict.keys()))

    def replace(self, match):
        return self.contractions_dict[match.group(0)]

    def expand_contractions(self, text):
        return self.contractions_re.sub(ExpandContractionsDialoguePreProcessorImpl.replace, text)

    def preprocess_operation(self, args):
        return [ExpandContractionsDialoguePreProcessorImpl.expand_contractions(text) for text in args]

    def parse(self, args):
        return True
