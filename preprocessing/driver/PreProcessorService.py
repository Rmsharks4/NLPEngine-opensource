import logging

from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class PreProcessorService:

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @classmethod
    def __check_input_parameters_type(cls, args):
        pass

    @classmethod
    def __check_input_parameters_existence(cls, args):
        pass

    @classmethod
    def preprocess_data(cls, args):
        pass
