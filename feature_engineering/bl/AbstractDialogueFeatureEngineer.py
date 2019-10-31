import abc
import logging
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl


class AbstractDialogueFeatureEngineer(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()

    @classmethod
    def engineer_feature(cls, args):
        if cls.engineer_feature_validation(args):
            cls.engineer_feature_operation(args)

    @classmethod
    def engineer_feature_validation(cls, args):
        return True

    def engineer_feature_operation(self, args):
        pass
