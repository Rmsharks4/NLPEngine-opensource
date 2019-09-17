
import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractPreProcessorDAO(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @abc.abstractmethod
    def load_data(self, args):
        pass

    @abc.abstractmethod
    def save_data(self, args):
        pass
