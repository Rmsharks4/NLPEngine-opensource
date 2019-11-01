"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Split Joint Words**:
splits combination words into two (well-managed to well managed, etc.)

"""

from data.bl.PlainTextDataImpl import PlainTextDataImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.SplitsDictionary import SplitsDictionary


class SplitJointWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Split Joint Words Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = [[PlainTextDataImpl.__name__]]
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_args = SplitsDictionary.__name__

    @classmethod
    def split_joint_words(cls, text, splits):
        """

        :param text: (str) string to examine
        :param splits: (SplitsDictionary) splits utils
        :return: (str) preprocessed data
        """

        def replace(match):
            return splits.splits_dict[match.group(0)]
        return splits.splits_re.sub(replace, str(text))

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (LowercaseDialoguePreProcessorImpl)
        (SplitsDictionary)
        :return: (list) array of preprocessed data
        """
        return args[PlainTextDataImpl.__name__].apply(
            lambda x: self.split_joint_words(x, args[self.config_pattern.properties.req_args]))
