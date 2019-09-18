# Main Function Here:
# PreProcess()
# Input: An array of dialogues
# Returns an array of dialogues

import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger


class Abstract_Dialogue_Batch_PreProcessor(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingLogger.__class__.__name__)

    @abc.abstractmethod
    def preprocess_batch(self, args):
        pass
