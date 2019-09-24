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
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.SplitsDictionary import SplitsDictionary


class SplitJointWordsPreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = LowercaseDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = SplitsDictionary.__name__

    @classmethod
    def split_joint_words(cls, text, splits):
        return text if text not in splits.splits_dict else splits.splits_replace

    def preprocess_operation(self, args):
        return [self.split_joint_words(args[self.config_pattern.properties.req_data],
                                       args[self.config_pattern.properties.req_args])]
