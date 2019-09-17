import abc
import logging
from feature_engineering.utils.FeatureEngineeringConstants import FeatureEngineeringConstants


class AbstractDialogueFeatureEngineer(metaclass=abc.ABCMeta):

    def __init__(self, args):
        self.logger = logging.getLogger(FeatureEngineeringConstants.LOGGER_NAME)
        self.req_args = args
        self.req_data = list()

    @classmethod
    def engineer_feature(cls, args):
        if cls.engineer_feature_validation(args):
            cls.engineer_feature_operation(args)

    @classmethod
    def engineer_feature_validation(cls, args):
        return True

    @abc.abstractmethod
    def engineer_feature_operation(self, args):
        pass
