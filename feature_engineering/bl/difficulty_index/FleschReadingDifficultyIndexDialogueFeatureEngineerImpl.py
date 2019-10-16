from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class FleschReadingDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        num_of_syllables = self.get_num_of_syllables(args[1])
        num_of_sentences = self.get_num_of_sentences(args[0])
        num_of_words = MathematicsUtils.length(args[1])
        avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        avg_syllables_per_word = MathematicsUtils.divide([num_of_syllables, num_of_words])
        return MathematicsUtils.subtract([
            206.835, MathematicsUtils.subtract([
                MathematicsUtils.multiply([
                    1.015, avg_sentence_length
                ]), MathematicsUtils.multiply([
                    84.6, avg_syllables_per_word
                ])
            ])
        ])
