
import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractDAO(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @abc.abstractmethod
    def load(self, args):
        pass

    @abc.abstractmethod
    def save(self, args):
        pass
