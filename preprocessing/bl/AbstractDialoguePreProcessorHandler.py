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
from preprocessing.utils.UtilsFactory import UtilsFactory
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from commons.dao.PandasDAOImpl import PandasDAOImpl
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from commons.config.AbstractConfig import AbstractConfig
import pandas as pd


class AbstractDialoguePreProcessingHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        """
        initializes Abstract Dialogue PreProcessor Handler: starts logger!
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def perform_preprocessing(self, args):
        """

        :param args: arguments needed for pre-processing pipeline
        """
        pass

    def validation(self, args):

        # IF ARGS IS NONE:
        if args is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', dict)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', dict)

        # IF ARGS IS NOT A DICT:
        if not isinstance(args, dict):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', dict)
            raise InvalidInfoException('Given:', type(args), 'Required:', dict)

        # IF ABSTRACT_DIALOGUE_PREPROCESSOR IS NOT IN ARGS:
        if AbstractDialoguePreProcessor.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.keys(), 'Required:', AbstractDialoguePreProcessor.__name__)
            raise MissingMandatoryFieldException('Given:', args.keys(),
                                                 'Required:', AbstractDialoguePreProcessor.__name__)

        # IF ABSTRACT_DIALOGUE_PREPROCESSOR IN ARGS IS NONE:
        if args[AbstractDialoguePreProcessor.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', list)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', list)

        # ABSTRACT_DIALOGUE_PREPROCESSOR IN ARGS IS NOT OF REQUIRED DATA TYPE:
        if not isinstance(args[AbstractDialoguePreProcessor.__name__], list):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args[AbstractDialoguePreProcessor.__name__]),
                              'Required:', list)
            raise InvalidInfoException('Given:', type(args[AbstractDialoguePreProcessor.__name__]),
                                       'Required:', list)

        # FOR CONFIG IN ABSTRACT_DIALOGUE_PREPROCESSOR IN ARGS:
        for config in args[AbstractDialoguePreProcessor.__name__]:

            # IF CONFIG IS NONE:
            if config is None:
                self.logger.error(MissingMandatoryFieldException.__name__,
                                  'Given:', None, 'Required:', AbstractConfig)
                raise MissingMandatoryFieldException('Given:', None, 'Required:', AbstractConfig)

            # IF CONFIG IN ARGS IS NOT OF REQUIRED DATA TYPE:
            if not isinstance(config, AbstractConfig):
                self.logger.error(InvalidInfoException.__name__,
                                  'Given:', type(config), 'Required:', AbstractConfig)
                raise InvalidInfoException('Given:', type(config), 'Required:', AbstractConfig)

        # IF PANDAS_DAO_IMPL NOT IN ARGS:
        if PandasDAOImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.keys(), 'Required:', PandasDAOImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.keys(), 'Required:', PandasDAOImpl.__name__)

        # IF PANDAS_DAO_IMPL IN ARGS IS NONE:
        if args[PandasDAOImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', pd.DataFrame)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', pd.DataFrame)

        # IF PANDAS_DAO_IMPL IN ARGS IS NOT OF REQUIRED DATA TYPE:
        if not isinstance(args[PandasDAOImpl.__name__], pd.DataFrame):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args[PandasDAOImpl.__name__]), 'Required:', pd.DataFrame)
            raise InvalidInfoException('Given:', type(args[PandasDAOImpl.__name__]), 'Required:', pd.DataFrame)

        # ALL CASES POSITIVE
        return True
