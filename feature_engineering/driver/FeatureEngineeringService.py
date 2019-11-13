
import pandas as pd
import logging
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from commons.dao.PandasDAOImpl import PandasDAOImpl
from feature_engineering.bl.AbstractDialogueFeatureEngineerHandlerFactory import AbstractDialogueFeatureEngineerHandlerFactory
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from commons.config.AbstractConfig import AbstractConfig
from feature_engineering.utils.FeatureEngineeringLogger import FeatureEngineeringLogger


class FeatureEngineeringService:

    def __init__(self):
        """
        initializes Feature-Engineer service class and starts logger.
        """
        self.logger = logging.getLogger(FeatureEngineeringLogger.__name__)

    def run(self, args):
        handler_obj = AbstractDialogueFeatureEngineerHandlerFactory.get_dialogue_feature_engineer_handler(
            StandardFlowDialogueFeatureEngineerHandlerImpl.__name__)

        return handler_obj.perform_feature_engineering({
            AbstractDialogueFeatureEngineer.__name__: args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__],
            PandasDAOImpl.__name__: args[PandasDAOImpl.__name__]
        })

    def validation(self, args):
        if args is None:
            self.logger.error(MissingMandatoryFieldException.__name__, 'Given:', type(None))
            raise MissingMandatoryFieldException('Given:', type(None))
        if not isinstance(args, dict):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', type(dict))
            raise InvalidInfoException('Given:', type(args), 'Required:', type(dict))
        if StandardFlowDialogueFeatureEngineerHandlerImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(),
                              'Required:', StandardFlowDialogueFeatureEngineerHandlerImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(),
                                                 'Required:', StandardFlowDialogueFeatureEngineerHandlerImpl.__name__)
        if args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(list))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(list))
        if not isinstance(args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__], list):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__]),
                              'Required:', type(list))
            raise InvalidInfoException('Given:', type(args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__]),
                                       'Required:', type(list))
        for config in args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__]:
            if not isinstance(config, AbstractConfig):
                self.logger.error(InvalidInfoException.__name__,
                                  'Given:', type(config), 'Required:', type(AbstractConfig))
                raise InvalidInfoException('Given:', type(config), 'Required:', type(AbstractConfig))
        if PandasDAOImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
        if args[PandasDAOImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(pd.DataFrame))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(pd.DataFrame))
        return True
