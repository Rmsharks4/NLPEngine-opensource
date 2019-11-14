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
import pandas as pd
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException


class SplitJointWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Split Joint Words Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = [[PlainTextDataImpl.__name__]]
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_args = SplitsDictionary.__name__

    def preprocess_operation(self, text, utils):
        def replace(match):
            return utils.splits_dict[match.group(0)]
        return utils.splits_re.sub(replace, str(text))

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
