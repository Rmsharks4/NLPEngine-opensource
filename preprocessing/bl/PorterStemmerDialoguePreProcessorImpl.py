
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import nltk

PorterStemmer = nltk.PorterStemmer()


class PorterStemmerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def stem(cls, text):
        return PorterStemmer.stem(text)

    @classmethod
    def preprocess_operation(cls, args):
        return [PorterStemmerDialoguePreProcessorImpl.stem(text) for text in args]
