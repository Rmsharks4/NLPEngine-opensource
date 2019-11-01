from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from feature_engineering.utils.TextStats import TextStats
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl


class SmogDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        return args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(lambda x: self.workmath({
            TokenTagsDialogueFeatureEngineerImpl.__name__: x,
            TextStats.__name__: args[TextStats.__name__]
        }))

    def workmath(self, args):
        num_of_sentences = self.get_num_of_sentences(args)
        num_of_polysyllables = self.get_num_of_polysyllables(args)
        return MathematicsUtils.add([
            3.1291, MathematicsUtils.multiply([
                1.043 * 0.5, MathematicsUtils.multiply([
                    30, MathematicsUtils.divide([
                        num_of_polysyllables, num_of_sentences
                    ])
                ])
            ])
        ])
