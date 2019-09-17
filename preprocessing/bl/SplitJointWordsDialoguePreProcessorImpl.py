
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class SplitJointWordsPreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def split_joint_words(cls, text):
        return text.replace('-', ' ')

    @classmethod
    def preprocess_operation(cls, args):
        return [SplitJointWordsPreProcessorImpl.split_joint_words(text) for text in args]