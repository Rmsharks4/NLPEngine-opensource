
import logging

from feature_engineering.bl.AbstractDialogueFeatureEngineerFactory import AbstractDialogueFeatureEngineerFactory
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from commons.dao.AbstractDAOFactory import AbstractDAOFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl
from commons.AbstractService import AbstractService
from feature_engineering.bl.AbstractDialogueFeatureEngineerHandlerFactory import AbstractDialogueFeatureEngineerHandlerFactory
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl


class FeatureEngineeringService(AbstractService):

    def __init__(self):
        """
        initializes Feature-Engineer service class and starts logger.
        """

    def run(self, args):
        dao_obj = AbstractDAOFactory.get_dao(SparkDAOImpl.__name__)
        data_obj = dao_obj.load([
            args[SparkDAOImpl.__name__], FeatureEngineeringService.__name__
        ])

        handler_obj = AbstractDialogueFeatureEngineerHandlerFactory.get_dialogue_feature_engineer_handler(
            StandardFlowDialogueFeatureEngineerHandlerImpl.__name__)
        output_obj = handler_obj.perform_preprocessing({
            AbstractDialogueFeatureEngineer.__name__: args[StandardFlowDialogueFeatureEngineerHandlerImpl.__name__],
            SparkDAOImpl.__name__: data_obj
        })

        return dao_obj.save([
            output_obj, args[SparkDAOImpl.__name__]
        ])
