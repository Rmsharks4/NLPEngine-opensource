import pandas as pd
import abc
import logging
from feature_engineering.utils.FeatureEngineeringLogger import FeatureEngineeringLogger
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from feature_engineering.utils.AbstractUtils import AbstractUtils


class AbstractDialogueFeatureEngineer(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(FeatureEngineeringLogger.__name__)

    def engineer_feature(self, args):
        try:
            if self.engineer_feature_validation(args):
                return self.engineer_feature_operation(args)
        except (MissingMandatoryFieldException, InvalidInfoException, DataFrameException) as exp:
            raise CommonBaseException(exp)

    def engineer_feature_operation(self, args):
        pass

    def engineer_feature_validation(self, args):
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
