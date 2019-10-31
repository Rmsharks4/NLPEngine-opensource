import logging
from feature_engineering.bl.StandardFlowConversationFeatureEngineerHandlerImpl import StandardFlowConversationFeatureEngineerHandlerImpl


class AbstractConversationFeatureEngineerHandlerFactory:

    @staticmethod
    def get_dialogue_feature_engineer_handler(handler_type):
        switcher = {
            StandardFlowConversationFeatureEngineerHandlerImpl.__name__: StandardFlowConversationFeatureEngineerHandlerImpl()
        }
        return switcher.get(handler_type, None)
