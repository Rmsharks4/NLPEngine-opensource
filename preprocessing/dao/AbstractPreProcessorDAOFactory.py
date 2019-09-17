
import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractPreProcessorDAOFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @classmethod
    def get_preprocessor_dao(cls, database_dialect):
        pass
