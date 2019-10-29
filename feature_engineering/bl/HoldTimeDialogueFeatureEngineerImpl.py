from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from data.bl.StartTimeDataImpl import StartTimeDataImpl
from data.bl.EndTimeDataImpl import EndTimeDataImpl
from data.bl.ConversationIDDataImpl import ConversationIDDataImpl


class HoldTimeDialogueFeatureEngineer(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [ConversationIDDataImpl.__name__,
                                                   StartTimeDataImpl.__name__,
                                                   EndTimeDataImpl.__name__]
        self.config_pattern.properties.req_args = None

    def engineer_feature_operation(self, args):
        hold_time = []
        for cid in args[ConversationIDDataImpl.__name__]:
            hold_time.append(MathematicsUtils.set_value(
                [MathematicsUtils.subtract([args[EndTimeDataImpl.__name__]
                                           .where(args[ConversationIDDataImpl] == cid),
                                           args[StartTimeDataImpl.__name__]
                                           .where(args[ConversationIDDataImpl] == cid)]), 0, 0, '<']))
        return hold_time
