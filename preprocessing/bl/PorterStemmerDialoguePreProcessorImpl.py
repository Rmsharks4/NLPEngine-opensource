"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Porter Stemmer**:
stems words to their origin stems (grows to grow, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.utils.PorterStemmer import PorterStemmer


class PorterStemmerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Porter Stemmer Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = PorterStemmer.__name__

    @classmethod
    def stem(cls, text, stemmer):
        """

        :param text: (str) string to examine
        :param stemmer: (PorterStemmer) stemmer utils
        :return: (str) preprocessed data
        """
        return stemmer.stemmer_lib.stem(text)

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (RemoveStopWordsDialoguePreProcessorImpl)(SpellCheckerDialoguePreProcessorImpl)
        (PorterStemmer)
        :return: (list) array of preprocessed data
        """
        return [self.stem(args[self.config_pattern.properties.req_data],
                          args[self.config_pattern.properties.req_args])]
