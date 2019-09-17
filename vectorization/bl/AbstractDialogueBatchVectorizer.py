# select a factory class based on input - and then do batch processing on it!
# should there be separate classes for each batch functions or inside same class call the separate function - weird
# example, in lookup - on its own its just going to iterate once and create a count vector
# once all the words are done, you want to make a dictionary with the smallest idx of the most occurring words and so on
# then you want a reverse dictionary - that finds the index given a word!
# make a two way dictionary for that case scenario
# aur ab dekhna yeh hai kay what function can i use to check if this is a batch process or a singular process

from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.bl.AbstractDialogueVectorizerFactory import AbstractDialogueVectorizerFactory
from vectorization.utils.MathematicsUtils import MathematicsUtils
from vectorization.utils.VectorizationConstants import VectorizationConstants
import logging


class AbstractDialogueBatchVectorizer:

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)
        self.dialogue_vectorizers = []

    @property
    def dialogue_vectorizers(self):
        return self.dialogue_vectorizers

    @dialogue_vectorizers.setter
    def dialogue_vectorizers(self, args):
        self.dialogue_vectorizers = args

    def batch_vectorize(self, args):
        for arg in args[0]:
            self.dialogue_vectorizers.append(AbstractDialogueVectorizerFactory.get_dialogue_vectorizer(arg))
        for arg in args[1]:
            for vectorizer in self.dialogue_vectorizers:
                self.dialogue_vectorizers[vectorizer].vectorize(arg)
        for vectorizer in self.dialogue_vectorizers:
            self.dialogue_vectorizers[vectorizer].aggregate()
