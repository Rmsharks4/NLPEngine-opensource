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
import pandas as pd
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException


class RemovePunctuationDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Punctuation Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_data = [[RemoveEmailsDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = PunctuationDictionary.__name__

    def preprocess_operation(self, text, utils):
        return utils.punctuation_replace.join([char for char in text if char not in utils.punctuation_dict])

    def preprocess_validation(self, args):

        # TRY THIS:
        try:

            # IF INITIAL VALIDATION SUCCESSFUL:
            if super().preprocess_validation(args):

                # FOR ALL REQ_INPUT:
                if self.config_pattern.properties.req_input is not None:
                    for arr in self.config_pattern.properties.req_input:
                        for elem in arr:

                            # IF ROW-WISE ELEMENT IN ARGS IS NOT OF REQUIRED DATA TYPE:
                            if args[elem].dtype != str:

                                # ERROR:
                                self.logger.error(InvalidInfoException.__name__,
                                                  'Given:', args[elem].dtype, 'Required:', str)
                                raise InvalidInfoException('Given:', args[elem].dtype, 'Required:', str)

                # FOR ALL REQ_DATA:
                if self.config_pattern.properties.req_data is not None:
                    for arr in self.config_pattern.properties.req_data:
                        for elem in arr:

                            # IF ROW-WISE ELEMENT IN ARGS IS NOT OF REQUIRED DATA TYPE:
                            if args[elem].dtype != str:

                                # ERROR:
                                self.logger.error(InvalidInfoException.__name__,
                                                  'Given:', args[elem].dtype, 'Required:', str)
                                raise InvalidInfoException('Given:', args[elem].dtype, 'Required:', str)

                # ALL CASES POSITIVE
                return True

        # CATCH ERRORS:
        except (MissingMandatoryFieldException, InvalidInfoException) as exp:
            raise CommonBaseException(exp)
