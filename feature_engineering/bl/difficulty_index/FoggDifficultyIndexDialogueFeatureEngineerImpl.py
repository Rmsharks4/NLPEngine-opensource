from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class FoggDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        difficult_words = self.get_difficult_words(args[1])
        num_of_difficult_words = MathematicsUtils.length(difficult_words)
        num_of_sentences = self.get_num_of_sentences(args[0])
        num_of_words = MathematicsUtils.length(args[1])
        avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        return MathematicsUtils.add(
            [MathematicsUtils.add(
                [MathematicsUtils.add(
                    [MathematicsUtils.multiply(
                        [MathematicsUtils.divide(
                            [num_of_words,
                             num_of_difficult_words]),
                            100]),
                        avg_sentence_length]),
                    5]),
                0.4])
