"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Word Net Lemmatizer**:
lemmatizes words to their roots (grew to grow, etc.)

"""

from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.WordnetLemmatizer import WordnetLemmatizer
import re


class WordNetLemmatizerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Word Net Lemmatizer Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = WordnetLemmatizer.__name__

    @classmethod
    def lemmatize(cls, text, lemmatizer):
        """

        :param text: (str) string to examine
        :param lemmatizer: (WordnetLemmatizer) lemmatizer utils
        :return:
        """
        return ' '.join(lemmatizer.lemmatizer_lib.lemmatize(x, pos=lemmatizer.lemmatize_mode) for x in re.split('[\s,]+', text))

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (RemoveStopWordsDialoguePreProcessorImpl) (SpellCheckerDialoguePreProcessorImpl)
        (WordnetLemmatizer)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.lemmatize(args[req_data], args[self.config_pattern.properties.req_args])
        return None
