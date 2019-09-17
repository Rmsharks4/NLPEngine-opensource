
import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractDialoguePreProcessingHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @abc.abstractmethod
    def perform_preprocessing(self, args):
        pass
