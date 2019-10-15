"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Split Joint Words**:
splits combination words into two (well-managed to well managed, etc.)

"""

from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
from preprocessing.bl.PlainTextDialoguePreProcessorImpl import PlainTextDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.SplitsDictionary import SplitsDictionary


class SplitJointWordsPreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Split Joint Words Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = [PlainTextDialoguePreProcessorImpl.__name__,
                                                   LowercaseDialoguePreProcessorImpl.__name__]
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
        return splits.splits_re.sub(replace, text)

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (LowercaseDialoguePreProcessorImpl)
        (SplitsDictionary)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.split_joint_words(args[req_data], args[self.config_pattern.properties.req_args])
        return None
