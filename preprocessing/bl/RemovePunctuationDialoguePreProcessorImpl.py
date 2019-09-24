"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Remove Punctuation**:
remove all punctuation from text (a,b,c to a b c)

"""

from preprocessing.utils.PunctuationDictionary import PunctuationDictionary
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl


class RemovePunctuationDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemoveEmailsDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = PunctuationDictionary.__name__

    @classmethod
    def remove_punctuation(cls, text, punctuation):
        return punctuation.punctuation_replace.join([char for char in text if char not in punctuation.punctuation_dict])

    def preprocess_operation(self, args):
        return [self.remove_punctuation(args[self.config_pattern.properties.req_data],
                                        args[self.config_pattern.properties.req_args])]
