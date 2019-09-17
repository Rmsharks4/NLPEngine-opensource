from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class WordsPerMinuteDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        num_of_words = MathematicsUtils.length(args[0])
        num_of_words_per_duration = MathematicsUtils.divide([num_of_words, args[1]])
        return MathematicsUtils.multiply([num_of_words_per_duration, 60])

