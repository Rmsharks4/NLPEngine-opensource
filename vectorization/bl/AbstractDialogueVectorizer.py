from vectorization.utils.VectorizationConstants import VectorizationConstants
import logging
import abc


class AbstractDialogueVectorizer:

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)
        self.data_structure = None

    @property
    def data_structure(self):
        return self.data_structure

    @data_structure.setter
    def data_structure(self, args):
        self.data_structure = args

    @classmethod
    def vectorize(cls, args):
        if cls.vectorize_validation(args):
            cls.vectorize_operation(args)

    @classmethod
    def vectorize_validation(cls, args):
        return args

    @abc.abstractmethod
    def vectorize_operation(self, args):
        pass

    @abc.abstractmethod
    def aggregate(self):
        pass
