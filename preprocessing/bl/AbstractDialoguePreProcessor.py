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


class AbstractDialoguePreProcessor(StandardConfigParserImpl):

    def __init__(self):
        """
        initialize abstract dialogue preprocessor: starts logger!
        """
        super().__init__()
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def preprocess(self, args):
        """

        :param args: arguments required for pre-processing!
        """
        try:
            if self.preprocess_validation(args):
                return self.preprocess_operation(args)
        except (MissingMandatoryFieldException, InvalidInfoException, DataFrameException) as exp:
            raise CommonBaseException(exp)

    def preprocess_operation(self, args):
        """

        :param args: arguments required for pre-processing!
        """
        pass

    def preprocess_validation(self, args):
        """

        :param args: arguments required for pre-processing!
        :return: True if correct else throws exception
        """
        if args is None:
            self.logger.error(MissingMandatoryFieldException.__name__, 'Given:', type(None))
            raise MissingMandatoryFieldException('Given:', type(None))
        if not isinstance(args, dict):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', type(dict))
            raise InvalidInfoException('Given:', type(args), 'Required:', type(dict))
        if self.config_pattern.properties.req_input is not None:
            for arr in self.config_pattern.properties.req_input:
                for elem in arr:
                    if elem not in args:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.items(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', elem)
                    if args[elem] is None:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', type(None), 'Required:', type(pd.Series))
                        raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(pd.Series))
        if self.config_pattern.properties.req_data is not None:
            for arr in self.config_pattern.properties.req_data:
                for elem in arr:
                    if elem not in args:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.items(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', elem)
                    if args[elem] is None:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', type(None), 'Required:', type(pd.Series))
                        raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(pd.Series))
        if self.config_pattern.properties.req_args is not None:
            for arr in self.config_pattern.properties.req_args:
                for elem in arr:
                    if elem not in args:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', args.items(), 'Required:', elem)
                        raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', elem)
                    if args[elem] is None:
                        self.logger.error(MissingMandatoryFieldException.__name__,
                                          'Given:', type(None), 'Required:', type(AbstractUtils))
                        raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(AbstractUtils))
        return True
