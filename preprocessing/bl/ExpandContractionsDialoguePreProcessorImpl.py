"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Expand Contractions**:
expands contractions in text (I'm to I am, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsPreProcessorImpl
from preprocessing.utils.ContractionsDictionary import ContractionsDictionary


class ExpandContractionsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Expand Contractions Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()

        self.logger.info('Setting Arguments in: ' + self.config_pattern.properties.__class__.__name__)
        self.config_pattern.properties.req_data = [SplitJointWordsPreProcessorImpl.__name__]
        self.logger.info("Required Data: " + SplitJointWordsPreProcessorImpl.__name__)
        self.config_pattern.properties.req_args = ContractionsDictionary.__name__
        self.logger.info("Required Arguments: " + ContractionsDictionary.__name__)

    def expand_contractions(self, text, contractions):
        """

        :param text: (str) string to examine
        :param contractions: (ContractionsDictionary) contractions utils
        :return: (str) preprocessed data
        """
        def replace(match):
            return contractions.contractions_dict[match.group(0)]
        return contractions.contractions_re.sub(replace, text)

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (ContractionsDictionary)
        (SplitJointWordsPreProcessorImpl)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.expand_contractions(args[req_data], args[self.config_pattern.properties.req_args])
        return None
