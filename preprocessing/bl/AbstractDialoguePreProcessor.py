"""
    Created By: Ramsha Siddiqui
    Description: This is the Abstract Dialogue Pre Processing Class -
    A Dialogue is a thread by any one of the speakers at a time.
"""

import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class AbstractDialoguePreProcessor(metaclass=abc.ABCMeta):

    def __init__(self, args):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)
        self.req_args = args
        self.req_data = list()

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
