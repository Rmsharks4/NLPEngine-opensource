"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects which implementation should be used at a given time:
- get_dialogue_preprocessor (pass in class name as argument)

"""

import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
from preprocessing.bl.PorterStemmerDialoguePreProcessorImpl import PorterStemmerDialoguePreProcessorImpl
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsPreProcessorImpl
from preprocessing.bl.WordNetLemmatizerDialoguePreProcessorImpl import WordNetLemmatizerDialoguePreProcessorImpl


class AbstractDialoguePreProcessorFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        """
        initializes abstract dialogue preprocessor factory: starts logger!
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @staticmethod
    def get_dialogue_preprocessor(preprocessor_type):
        """

        :param preprocessor_type: (str) AbstractDialoguePreProcessorImpl class name
        :return: (AbstractDialoguePreProcessor) else throws Exception
        """
        switcher = {
            ExpandContractionsDialoguePreProcessorImpl.__name__: ExpandContractionsDialoguePreProcessorImpl(),
            LowercaseDialoguePreProcessorImpl.__name__: LowercaseDialoguePreProcessorImpl(),
            PorterStemmerDialoguePreProcessorImpl.__name__: PorterStemmerDialoguePreProcessorImpl(),
            RemoveEmailsDialoguePreProcessorImpl.__name__: RemoveEmailsDialoguePreProcessorImpl(),
            RemoveNumericCharactersDialoguePreProcessorImpl.__name__: RemoveNumericCharactersDialoguePreProcessorImpl(),
            RemovePunctuationDialoguePreProcessorImpl.__name__: RemovePunctuationDialoguePreProcessorImpl(),
            RemoveStopWordsDialoguePreProcessorImpl.__name__: RemoveStopWordsDialoguePreProcessorImpl(),
            SpellCheckerDialoguePreProcessorImpl.__name__: SpellCheckerDialoguePreProcessorImpl(),
            SplitJointWordsPreProcessorImpl.__name__: SplitJointWordsPreProcessorImpl(),
            WordNetLemmatizerDialoguePreProcessorImpl.__name__: WordNetLemmatizerDialoguePreProcessorImpl()
        }

        return switcher.get(preprocessor_type, '')
