import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.TextStats import TextStats


class AbstractDifficultyIndexDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[TokenTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_args = TextStats.__name__

    def engineer_feature_operation(self, args):
        return self.difficulty_index(args)

    def difficulty_index(self, args):
        pass

    @classmethod
    def get_difficult_words(cls, args):
        difficult_words = []
        for word in args[TokenTagsDialogueFeatureEngineerImpl.__name__]:
            if str(word) not in args[TextStats.__name__].es and args[TextStats.__name__].ts.syllable_count(str(word)) > 2:
                difficult_words.append(word)
        return difficult_words

    @classmethod
    def get_num_of_sentences(cls, args):
        return args[TextStats.__name__].ts.sentence_count(' '.join(token.text for token in args[TokenTagsDialogueFeatureEngineerImpl.__name__]))

    @classmethod
    def get_num_of_syllables(cls, args):
        num_of_syllables = 0
        for word in args[TokenTagsDialogueFeatureEngineerImpl.__name__]:
            num_of_syllables += args[TextStats.__name__].ts.syllable_count(str(word))
        return num_of_syllables

    @classmethod
    def get_num_of_polysyllables(cls, args):
        num_of_polysyllables = 0
        for word in args[TokenTagsDialogueFeatureEngineerImpl.__name__]:
            syllable_count = args[TextStats.__name__].ts.syllable_count(str(word))
            if syllable_count >= 3:
                num_of_polysyllables += 1
        return num_of_polysyllables
