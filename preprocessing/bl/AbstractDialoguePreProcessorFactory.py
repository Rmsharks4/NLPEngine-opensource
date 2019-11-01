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
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsDialoguePreProcessorImpl
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from preprocessing.bl.WordNetLemmatizerDialoguePreProcessorImpl import WordNetLemmatizerDialoguePreProcessorImpl
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl


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
        switcher = dict()
        for y in AbstractDialoguePreProcessor().__class__.__subclasses__():
            switcher[y.__name__] = y()
            switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))
        return switcher.get(preprocessor_type, None)
