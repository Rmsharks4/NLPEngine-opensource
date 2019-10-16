from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class DaleChallaDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        difficult_words = self.get_difficult_words(args[1])
        num_of_difficult_words = MathematicsUtils.length(difficult_words)
        num_of_sentences = self.get_num_of_sentences(args[0])
        num_of_words = MathematicsUtils.length(args[1])
        avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        dale_challa_readability = MathematicsUtils.multiply([
            0.1579, MathematicsUtils.add([
                    MathematicsUtils.subtract([
                        100, MathematicsUtils.multiply([
                            MathematicsUtils.divide([
                                MathematicsUtils.subtract([
                                    num_of_words, num_of_difficult_words
                                ]), num_of_words
                            ]), 100
                        ])
                    ]), MathematicsUtils.multiply([
                        0.0496, avg_sentence_length
                    ])
            ])
        ])
        return MathematicsUtils.set_value([
            dale_challa_readability, 5, MathematicsUtils.add([
                dale_challa_readability, 3.6365
            ]), '>'
        ])
