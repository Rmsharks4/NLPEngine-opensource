import abc
import logging
from vectorization.utils.VectorizationConstants import VectorizationConstants


class AbstractDataStructure(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)
