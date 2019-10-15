
from feature_engineering.bl.AbstractDialogueFeatureEngineerHandler import AbstractDialogueFeatureEngineerHandler
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.AbstractDialogueFeatureEngineerFactory import AbstractDialogueFeatureEngineerFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl


class StandardFlowDialogueFeatureEngineerHandlerImpl(AbstractDialogueFeatureEngineerHandler):

    def __init__(self):
        """
        initializes Standard Flow Dialogue Pre-Processor Handler Implementation Class
        """
        super().__init__()

    def perform_feature_engineering(self, args):
        pass
