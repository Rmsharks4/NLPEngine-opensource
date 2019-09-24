
import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger


class AbstractDialoguePreProcessingHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @abc.abstractmethod
    def perform_preprocessing(self, args):
        pass
