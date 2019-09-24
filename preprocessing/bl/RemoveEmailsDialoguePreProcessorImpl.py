
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.EmailsDictionary import EmailsDictionary
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl


class RemoveEmailsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemoveNumericCharactersDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = EmailsDictionary.__name__

    @classmethod
    def remove_emails(cls, text, emails):
        text = emails.standard_re.sub(emails.replace_text, text)
        text = emails.semi_standard_re.sub(emails.replace_text, text)
        text = emails.non_standard_re.sub(emails.replace_text, text)
        return text

    def preprocess_operation(self, args):
        return [self.remove_emails(args[self.config_pattern.properties.req_data],
                                   args[self.config_pattern.properties.req_args])]
