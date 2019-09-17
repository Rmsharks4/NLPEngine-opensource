
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import nltk

stopwords = nltk.corpus.stopwords.words('english')


class RemoveStopWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def remove_stop_words(cls, text):
        return text if text not in stopwords else ''

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveStopWordsDialoguePreProcessorImpl.remove_stop_words(text) for text in args]
