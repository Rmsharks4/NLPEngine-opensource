
import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger


class AbstractDAO(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @abc.abstractmethod
    def load(self, args):
        pass

    @abc.abstractmethod
    def save(self, args):
        pass
