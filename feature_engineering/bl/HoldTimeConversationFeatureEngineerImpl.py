from feature_engineering.bl.AbstractConversationFeatureEngineer import AbstractConversationFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from data.bl.StartTimeDataImpl import StartTimeDataImpl
from data.bl.EndTimeDataImpl import EndTimeDataImpl
from data.bl.ConversationIDDataImpl import ConversationIDDataImpl


class HoldTimeDialogueFeatureEngineer(AbstractConversationFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[ConversationIDDataImpl.__name__,
                                                    StartTimeDataImpl.__name__,
                                                    EndTimeDataImpl.__name__]]
        self.config_pattern.properties.req_args = None

    def engineer_feature_operation(self, args):
        return MathematicsUtils.set_value([MathematicsUtils
                                          .subtract([args[EndTimeDataImpl.__name__],
                                                     args[StartTimeDataImpl.__name__]]), 0, 0, '<'])
