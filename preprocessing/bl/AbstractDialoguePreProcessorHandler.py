"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects in what flow the classes should be created and called:
- perform_preprocessing (pass in configurations and data elements)

"""

import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger


class AbstractDialoguePreProcessingHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        """
        initializes Abstract Dialogue PreProcessor Handler: starts logger!
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @abc.abstractmethod
    def perform_preprocessing(self, args):
        """

        :param args: arguments needed for pre-processing pipeline
        """
        pass
