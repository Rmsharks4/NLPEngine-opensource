
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import re
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl


class RemoveEmailsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemoveNumericCharactersDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None

    @classmethod
    def remove_emails(cls, text):
        text = re.sub(r'\w*@\w*\.\w*', '#', text)
        text = re.sub(r'\w*\.\w*', '#', text)
        text = re.sub(r'\w*\sdot\s\w*', '#', text)
        return text

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveEmailsDialoguePreProcessorImpl.remove_emails(text) for text in args]