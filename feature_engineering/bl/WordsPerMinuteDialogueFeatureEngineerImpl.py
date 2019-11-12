from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl
from data.bl.StartTimeDataImpl import StartTimeDataImpl
from data.bl.EndTimeDataImpl import EndTimeDataImpl
from feature_engineering.utils.WPMLimit import WPMLimit


class WordsPerMinuteDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[TokenTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = [[StartTimeDataImpl.__name__, EndTimeDataImpl.__name__]]
        self.config_pattern.properties.req_args = WPMLimit.__name__

    def engineer_feature_operation(self, args):
        num_of_words = args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(
            lambda x: int(MathematicsUtils.length(x)))
        args[StartTimeDataImpl.__name__] = args[StartTimeDataImpl.__name__].apply(
            lambda x: int(x))
        args[EndTimeDataImpl.__name__] = args[EndTimeDataImpl.__name__].apply(
            lambda x: int(x))
        duration = MathematicsUtils.add([args[StartTimeDataImpl.__name__],
                                         args[EndTimeDataImpl.__name__]])
        num_of_words_per_duration = MathematicsUtils.divide([num_of_words, duration])
        return MathematicsUtils.multiply([num_of_words_per_duration, args[WPMLimit.__name__].wpm])
