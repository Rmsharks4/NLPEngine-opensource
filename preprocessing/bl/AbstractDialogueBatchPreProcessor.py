# Main Function Here:
# PreProcess()
# Input: An array of dialogues
# Returns an array of dialogues

import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants

class Abstract_Dialogue_Batch_PreProcessor(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @abc.abstractmethod
    def preprocess_batch(self, args):
        pass
