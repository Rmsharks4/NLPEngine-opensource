"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- pre-process (operation and validation included!)

**Remove Emails**:
removes sensitive email info (abc@ab.com to EMAIL, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.EmailsDictionary import EmailsDictionary
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl


class RemoveEmailsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Emails Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveNumericCharactersDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = EmailsDictionary.__name__

    @classmethod
    def remove_emails(cls, text, emails):
        """

        :param text: (str) string to examine
        :param emails: (EmailsDictionary) emails utils
        :return: (str) preprocessed data
        """
        text = emails.standard_re.sub(emails.replace_text, text)
        text = emails.non_standard_re.sub(emails.replace_text, text)
        return text

    def preprocess_operation(self, args):
        """

        :param args: dict) contains req_data and req_args
        (RemoveNumericCharactersDialoguePreProcessorImpl)
        (EmailsDictionary)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.remove_emails(args[req_data], args[self.config_pattern.properties.req_args])
        return None
