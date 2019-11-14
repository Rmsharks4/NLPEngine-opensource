"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Word Net Lemmatizer**:
lemmatizes words to their roots (grew to grow, etc.)

"""

from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.WordnetLemmatizer import WordnetLemmatizer
import re
import pandas as pd
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException


class WordNetLemmatizerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Word Net Lemmatizer Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_data = [[RemoveStopWordsDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = WordnetLemmatizer.__name__

    def preprocess_operation(self, text, utils):
        return ' '.join(utils.lemmatizer_lib.lemmatize(x, pos=utils.lemmatize_mode) for x in re.split('[\s,]+', text))

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
