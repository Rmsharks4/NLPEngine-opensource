from feature_engineering.bl.difficulty_index.AbstractDifficultyIndexDialogueFeatureEngineerImpl import AbstractDifficultyIndexDialogueFeatureEngineerImpl
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from feature_engineering.utils.TextStats import TextStats
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl


class DaleChallaDifficultyIndexDialogueFeatureEngineerImpl(AbstractDifficultyIndexDialogueFeatureEngineerImpl):

    def difficulty_index(self, args):
        return args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(lambda x: self.workmath(
                                                             {TokenTagsDialogueFeatureEngineerImpl.__name__: x,
                                                              TextStats.__name__: args[TextStats.__name__]}))

    def workmath(self, args):
        difficult_words = self.get_difficult_words(args)
        num_of_difficult_words = MathematicsUtils.length(difficult_words)
        num_of_sentences = self.get_num_of_sentences(args)
        num_of_words = MathematicsUtils.length(args[TokenTagsDialogueFeatureEngineerImpl.__name__])
        if num_of_sentences > 0:
            avg_sentence_length = MathematicsUtils.divide([num_of_words, num_of_sentences])
        else:
            avg_sentence_length = 0
        if num_of_words > 0:
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
        else:
            dale_challa_readability = 0.1579*(100 + avg_sentence_length*0.0496)
        res = MathematicsUtils.set_value([
            dale_challa_readability, 5, MathematicsUtils.add([
                dale_challa_readability, 3.6365
            ]), '>'
        ])
        return res
