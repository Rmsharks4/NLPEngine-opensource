from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import nltk


class WordNet_Lemmatizer_Dialogue_PreProcessor_Impl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__class__.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__class__.__name__]
        self.config_pattern.properties.req_args = None
        self.WordNet_Lemmatizer = nltk.stem.WordNetLemmatizer()

    @classmethod
    def lemmatize(cls, text):
        return cls.WordNet_Lemmatizer.lemmatize(text, pos='v')

    @classmethod
    def preprocess_operation(cls, args):
        return [WordNet_Lemmatizer_Dialogue_PreProcessor_Impl.lemmatize(text) for text in args]
