"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

"""

import pandas as pd
import abc
import logging
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from preprocessing.utils.AbstractUtils import AbstractUtils
from preprocessing.utils.UtilsFactory import UtilsFactory


class AbstractDialoguePreProcessor(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def preprocess(self, args):

        # TRY THIS:
        try:

            # IF INITIAL VALIDATION SUCCESSFUL:
            if self.preprocess_validation(args):

                # CREATE RESULTANT DATAFRAME:
                res = pd.DataFrame()

                # FOR ALL REQ_INPUT:
                if self.config_pattern.properties.req_input is not None:
                    for arr in self.config_pattern.properties.req_input:
                        for elem in arr:

                            # PERFORM PREPROCESS OPERATION:
                            res = res.concat(args[elem].apply(
                                lambda x: self.preprocess_operation(x, args[self.config_pattern.properties.req_args])))

                # FOR ALL REQ_DATA:
                if self.config_pattern.properties.req_data is not None:
                    for arr in self.config_pattern.properties.req_data:
                        for elem in arr:

                            # PERFORM PREPROCESS OPERATION
                            res = res.concat(args[elem].apply(
                                lambda x: self.preprocess_operation(x, args[self.config_pattern.properties.req_args])))

                # RETURN RESULTANT DATAFRAME
                return res

        # CATCH ERRORS:
        except (MissingMandatoryFieldException, InvalidInfoException, DataFrameException) as exp:
            raise CommonBaseException(exp)

    def preprocess_operation(self, text, utils):
        pass

    def preprocess_validation(self, args):

        # IF ARGS IS NONE:
        if args is None:

            # ERROR:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', dict)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', dict)

        # IF ARGS IS NOT A DICT:
        if not isinstance(args, dict):

            # ERROR:
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', dict)
            raise InvalidInfoException('Given:', type(args), 'Required:', dict)

        # FOR ALL REQ_INPUT:
        if self.config_pattern.properties.req_input is not None:
            for arr in self.config_pattern.properties.req_input:
                for elem in arr:

                    # IF ELEMENT IS MISSING FROM ARGS:
                    if elem not in args:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.keys(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.keys(), 'Required:', elem)

                    # IF ELEMENT IN ARGS IS NONE:
                    if args[elem] is None:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', None, 'Required:', pd.Series)
                        raise MissingMandatoryFieldException('Given:', None, 'Required:', pd.Series)

                    # IF ELEMENT IN ARGS IS NOT OF REQUIRED DATA TYPE:
                    if not isinstance(args[elem], pd.Series):

                        # ERROR:
                        self.logger.error(InvalidInfoException.__name__,
                                          'Given:', type(args[elem]),
                                          'Required:', pd.Series)
                        raise InvalidInfoException('Given:', type(args[elem]),
                                                   'Required:', pd.Series)

        # FOR ALL REQ_DATA:
        if self.config_pattern.properties.req_data is not None:
            for arr in self.config_pattern.properties.req_data:
                for elem in arr:

                    # IF ELEMENT IS MISSING FROM ARGS:
                    if elem not in args:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.keys(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.keys(), 'Required:', elem)

                    # IF ELEMENT IN ARGS IS NONE:
                    if args[elem] is None:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', None, 'Required:', pd.Series)
                        raise MissingMandatoryFieldException('Given:', None, 'Required:', pd.Series)

                    # IF ELEMENT IN ARGS IS NOT OF REQUIRED DATA TYPE:
                    if not isinstance(args[elem], pd.Series):

                        # ERROR:
                        self.logger.error(InvalidInfoException.__name__,
                                          'Given:', type(args[elem]),
                                          'Required:', pd.Series)
                        raise InvalidInfoException('Given:', type(args[elem]),
                                                   'Required:', pd.Series)

        # FOR ALL REQ_ARGS:
        if self.config_pattern.properties.req_args is not None:
            for arr in self.config_pattern.properties.req_args:
                for elem in arr:

                    # IF ELEMENT IS MISSING FROM ARGS:
                    if elem not in args:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.keys(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.keys(), 'Required:', elem)

                    # IF ELEMENT IN ARGS IS NONE:
                    if args[elem] is None:

                        # ERROR:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', None, 'Required:', AbstractUtils)
                        raise MissingMandatoryFieldException('Given:', None, 'Required:', AbstractUtils)

                    # IF ELEMENT IN ARGS IS NOT OF REQUIRED DATA TYPE
                    if not isinstance(args[elem], type(UtilsFactory.get_utils(elem))):

                        # ERROR:
                        self.logger.error(InvalidInfoException.__name__,
                                          'Given:', type(args[elem]),
                                          'Required:', type(UtilsFactory.get_utils(elem)))
                        raise InvalidInfoException('Given:', type(args[elem]),
                                                   'Required:', type(UtilsFactory.get_utils(elem)))

        # ALL CASES POSITIVE
        return True
