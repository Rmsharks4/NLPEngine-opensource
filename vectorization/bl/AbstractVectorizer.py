from vectorization.utils.VectorizationConstants import VectorizationConstants
import logging
import abc


class AbstractVectorizer:

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)

    @abc.abstractmethod
    def vectorize(self, args):
        pass
