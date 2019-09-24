"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

"""

import abc
import logging
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger


class AbstractDialoguePreProcessor(StandardConfigParserImpl, metaclass=abc.ABCMeta):

    def __init__(self):
        """
        initialize abstract dialogue preprocessor: starts logger!
        """
        super().__init__()
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @classmethod
    def preprocess(cls, args):
        """
        a function to preprocess
        :param args: arguments required for pre-processing!
        """
        if cls.preprocess_validation(args):
            cls.preprocess_operation(args)

    @abc.abstractmethod
    def preprocess_operation(self, args):
        """
        abstract function that perform preprocessing
        :param args: arguments required for pre-processing!
        """
        pass

    @classmethod
    def preprocess_validation(cls, args):
        """

        :param args: function that validates preprocessing arguments
        :return: True if correct else throws exception
        """
        if isinstance(args, list):
            if args.dtype == str:
                return True
        return False
