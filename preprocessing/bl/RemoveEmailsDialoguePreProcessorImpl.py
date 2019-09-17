
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import re


class RemoveEmailsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def remove_emails(cls, text):
        text = re.sub(r'\w*@\w*\.\w*', '#', text)
        text = re.sub(r'\w*\.\w*', '#', text)
        text = re.sub(r'\w*\sdot\s\w*', '#', text)
        return text

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveEmailsDialoguePreProcessorImpl.remove_emails(text) for text in args]