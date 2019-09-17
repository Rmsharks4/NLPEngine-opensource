
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import nltk

WordNet_Lemmatizer = nltk.stem.WordNetLemmatizer()


class WordNet_Lemmatizer_Dialogue_PreProcessor_Impl(AbstractDialoguePreProcessor):

    @classmethod
    def lemmatize(cls, text):
        return WordNet_Lemmatizer.lemmatize(text, pos='v')

    @classmethod
    def preprocess_operation(cls, args):
        return [WordNet_Lemmatizer_Dialogue_PreProcessor_Impl.lemmatize(text) for text in args]
