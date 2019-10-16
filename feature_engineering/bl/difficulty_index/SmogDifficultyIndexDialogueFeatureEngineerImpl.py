from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class SmogDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        num_of_sentences = self.get_num_of_sentences(args[0])
        num_of_polysyllables = self.get_num_of_polysyllables(args[1])
        return MathematicsUtils.add([
            MathematicsUtils.multiply([
                1.043 * 0.5, MathematicsUtils.multiply([
                    30, MathematicsUtils.divide([
                        num_of_polysyllables, num_of_sentences
                    ])
                ])
            ])
        ])
