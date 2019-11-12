import logging
import abc
from vectorization.utils.VectorizationConstants import VectorizationConstants
from vectorization.bl.lookup.LookUpDialogueVectorizerImpl import LookUpDialogueVectorizer
from vectorization.bl.onehot.OneHotDialogueVectorizerImpl import OneHotDialogueVectorizer
from vectorization.bl.tfidf.TFIDFDialogueVectorizerImpl import TFIDFDialogueVectorizer
from vectorization.bl.embedding.EmbeddingDialogueVectorizerImpl import EmbeddingDialogueVectorizer


class AbstractDialogueVectorizerFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)

    @classmethod
    def get_dialogue_vectorizer(self, vectorizer_type):
        switcher = {
            LookUpDialogueVectorizer(): LookUpDialogueVectorizer.__class__.__name__,
            OneHotDialogueVectorizer(): OneHotDialogueVectorizer.__class__.__name__,
            TFIDFDialogueVectorizer(): TFIDFDialogueVectorizer.__class__.__name__,
            EmbeddingDialogueVectorizer(): EmbeddingDialogueVectorizer.__class__.__name__
        }
        return switcher.get(vectorizer_type, '')
