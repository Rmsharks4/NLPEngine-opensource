"""
    Created By: Ramsha Siddiqui
    Description: This is the Abstract Dialogue Pre Processing Class -
    A Dialogue is a thread by any one of the speakers at a time.
"""

import abc
import logging
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractDialoguePreProcessor(metaclass=abc.ABCMeta, StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @classmethod
    def preprocess(cls, args):
        """

        :param args:
        """
        if cls.preprocess_validation(args):
            cls.preprocess_operation(args)

    @abc.abstractmethod
    def preprocess_operation(self, args):
        pass

    @classmethod
    def preprocess_validation(cls, args):
        """

        :param args:
        :return:
        """
        if isinstance(args, list):
            if args.dtype == str:
                return True
        return False
