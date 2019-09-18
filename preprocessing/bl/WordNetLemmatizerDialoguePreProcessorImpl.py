from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.WordnetLemmatizer import WordnetLemmatizer


class WordNet_Lemmatizer_Dialogue_PreProcessor_Impl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__class__.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__class__.__name__]
        self.config_pattern.properties.req_args = WordnetLemmatizer.__class__.__name__

    @classmethod
    def lemmatize(cls, text, lemmatizer):
        return lemmatizer.lemmatizer_lib.lemmatize(text, pos=lemmatizer.lemmatizer_mode)

    def preprocess_operation(self, args):
        return [self.lemmatize(args[self.config_pattern.properties.req_data],
                               args[self.config_pattern.properties.req_args])]
