from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from feature_engineering.utils.TextStats import TextStats
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl


class FoggDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        return args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(lambda x: self.workmath({
            TokenTagsDialogueFeatureEngineerImpl.__name__: x,
            TextStats.__name__: args[TextStats.__name__]
        }))

    def workmath(self, args):
        difficult_words = self.get_difficult_words(args)
        num_of_difficult_words = MathematicsUtils.length(difficult_words)
        num_of_sentences = self.get_num_of_sentences(args)
        num_of_words = MathematicsUtils.length(args[TokenTagsDialogueFeatureEngineerImpl.__name__])
        avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        if num_of_difficult_words > 0:
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
        else:
            return 5.4 + avg_sentence_length
