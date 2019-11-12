

import logging
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from commons.dao.PandasDAOImpl import PandasDAOImpl
from feature_engineering.bl.AbstractDialogueFeatureEngineerHandlerFactory import AbstractDialogueFeatureEngineerHandlerFactory
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl


class FeatureEngineeringService:

    def __init__(self):
        """
        initializes Feature-Engineer service class and starts logger.
        """

    def run(self, args):
        handler_obj = AbstractDialogueFeatureEngineerHandlerFactory.get_dialogue_feature_engineer_handler(
            StandardFlowDialogueFeatureEngineerHandlerImpl.__name__)

        return handler_obj.perform_feature_engineering({
            AbstractDialogueFeatureEngineer.__name__: args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__],
            PandasDAOImpl.__name__: args[PandasDAOImpl.__name__]
        })
