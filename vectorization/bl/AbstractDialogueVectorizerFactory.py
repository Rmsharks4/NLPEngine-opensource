import logging
import abc
from vectorization.utils.VectorizationConstants import VectorizationConstants
from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.bl.lookup import *
from vectorization.bl.onehot import *
from vectorization.bl.count import *
from vectorization.bl.tfidf import *
from vectorization.bl.embedding import *


class AbstractDialogueVectorizerFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)

    @staticmethod
    def get_dialogue_vectorizer(vectorizer_type):
        switcher = dict()
        for y in AbstractDialogueVectorizer().__class__.__subclasses__():
            switcher[y.__name__] = y()
            switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))
        return switcher.get(vectorizer_type, None)
