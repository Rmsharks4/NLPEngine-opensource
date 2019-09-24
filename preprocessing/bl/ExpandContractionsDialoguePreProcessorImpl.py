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
        super().__init__()
        self.config_pattern.properties.req_data = SplitJointWordsPreProcessorImpl.__name__
        self.config_pattern.properties.req_args = ContractionsDictionary.__name__

    def replace(self, match, contractions_dict):
        return contractions_dict[match.group(0)]

    def expand_contractions(self, text, contractions):
        return contractions.contractions_re.sub(self.replace, text, contractions.contractions_dict)

    def preprocess_operation(self, args):
        return [self.expand_contractions(args[self.config_pattern.properties.req_data],
                                         args[self.config_pattern.properties.req_args])]
