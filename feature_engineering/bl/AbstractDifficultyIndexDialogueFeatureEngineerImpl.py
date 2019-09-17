import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from textstat.textstat import textstatistics, easy_word_set


class AbstractDifficultyIndexDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        return self.difficulty_index(args)

    @abc.abstractmethod
    def difficulty_index(self, args):
        pass

    @classmethod
    def get_difficult_words(cls, args):
        difficult_words = []
        for word in args:
            if word not in easy_word_set and textstatistics().syllable_count(word) > 2:
                difficult_words.append(word)
        return difficult_words

    @classmethod
    def get_num_of_sentences(cls, args):
        return textstatistics.sentence_count(args)

    @classmethod
    def get_num_of_syllables(cls, args):
        num_of_syllables = 0
        for word in args:
            num_of_syllables += textstatistics().syllable_count(word)
        return num_of_syllables

    @classmethod
    def get_num_of_polysyllables(cls, args):
        num_of_polysyllables = 0
        for word in args:
            syllable_count = textstatistics().syllable_count(word)
            if syllable_count >= 3:
                num_of_polysyllables += 1
        return num_of_polysyllables
