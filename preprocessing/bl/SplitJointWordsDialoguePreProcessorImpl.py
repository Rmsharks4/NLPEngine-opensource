from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class SplitJointWordsPreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = LowercaseDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None

    @classmethod
    def split_joint_words(cls, text):
        return text.replace('-', ' ')

    @classmethod
    def preprocess_operation(cls, args):
        return [SplitJointWordsPreProcessorImpl.split_joint_words(text) for text in args]