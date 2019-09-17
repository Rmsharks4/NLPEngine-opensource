
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from commons.config.PreProcessingConfigParserImpl import PreProcessingConfigParserImpl
import csv
import re


class ExpandContractionsDialoguePreProcessorImpl(AbstractDialoguePreProcessor, PreProcessingConfigParserImpl):

    def __init__(self, args):
        AbstractDialoguePreProcessor.__init__(self, args)
        PreProcessingConfigParserImpl.__init__(self)
        self.req_data.append('ConversationLowerJoin')
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
