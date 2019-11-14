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
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException


class AbstractDialoguePreProcessorFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        """
        initializes abstract dialogue preprocessor factory: starts logger!
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def get_dialogue_preprocessor(self, preprocessor_type):

        # TRY THIS:
        try:

            # IF INITIAL VALIDATION SUCCESSFUL:
            if self.validation(preprocessor_type):

                # GET REQUIRED PREPROCESSOR TYPE FROM DICT:
                switcher = dict()
                for y in AbstractDialoguePreProcessor().__class__.__subclasses__():
                    switcher[y.__name__] = y()
                    switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))

                # RETURN PREPROCESSOR CLASS IF EXISTS:
                return switcher.get(preprocessor_type, None)

        # CATCH ERRORS:
        except (MissingMandatoryFieldException, InvalidInfoException) as exp:
            raise CommonBaseException(exp)

    def validation(self, preprocessor_type):

        # IF PREPROCESSOR_TYPE IS NONE:
        if preprocessor_type is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', str)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', str)

        # IF PREPROCESSOR_TYPE IS NOT STRING:
        if not isinstance(preprocessor_type, str):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(preprocessor_type), 'Required:', str)
            raise InvalidInfoException('Given:', type(preprocessor_type), 'Required:', str)

        # IF PREPROCESSOR_TYPE NOT A CHILD OF ABSTRACT_DIALOGUE_PREPROCESSOR:
        if preprocessor_type not in [y.__name__ for y in AbstractDialoguePreProcessor().__class__.__subclasses__()]:
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', preprocessor_type,
                              'Required Value from :', [y.__name__ for y in
                                                        AbstractDialoguePreProcessor().__class__.__subclasses__()])
            raise InvalidInfoException('Given:', preprocessor_type,
                                       'Required Value from :', [y.__name__ for y in
                                                                 AbstractDialoguePreProcessor().__class__.__subclasses__()])

        # ALL CASES POSITIVE
        return True
