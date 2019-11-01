from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from feature_engineering.utils.TextStats import TextStats
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl


class FleschReadingDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        return args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(
            lambda x: self.workmath({TokenTagsDialogueFeatureEngineerImpl.__name__: x,
                                     TextStats.__name__: args[TextStats.__name__]}))

    def workmath(self, args):
        num_of_syllables = self.get_num_of_syllables(args)
        num_of_sentences = self.get_num_of_sentences(args)
        num_of_words = MathematicsUtils.length(args[TokenTagsDialogueFeatureEngineerImpl.__name__])
        avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        avg_syllables_per_word = MathematicsUtils.divide([num_of_syllables, num_of_words])
        res = MathematicsUtils.subtract([
            206.835, MathematicsUtils.subtract([
                MathematicsUtils.multiply([
                    1.015, avg_sentence_length
                ]), MathematicsUtils.multiply([
                    84.6, avg_syllables_per_word
                ])
            ])
        ])
        return res
