import logging
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl


class AbstractDialogueFeatureEngineerHandlerFactory:

    @staticmethod
    def get_dialogue_feature_engineer_handler(handler_type):
        switcher = {
            StandardFlowDialogueFeatureEngineerHandlerImpl.__name__: StandardFlowDialogueFeatureEngineerHandlerImpl()
        }
        return switcher.get(handler_type, None)
