"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class contains a 'run' function that runs the whole routine - starting from DAO to BL to DAO again.
- An implementation of **Abstract Service** in NLP.commons
- Implements the following main function: **run**

"""

import pandas as pd
import logging
from commons.config.AbstractConfig import AbstractConfig
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from commons.dao.PandasDAOImpl import PandasDAOImpl
from preprocessing.bl.AbstractDialoguePreProcessorHandlerFactory import AbstractDialoguePreProcessorHandlerFactory
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException


class PreProcessorService:

    def __init__(self):
        """
        initializes Pre-processor service class and starts logger.
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def run(self, args):
        """

        :param args: (dict) contains the following
        (list(Spark Data-frame))
        (StandardFlowDialoguePreProcessorHandlerImpl)
        :return: (SparkDAOImpl) DAO object to use further
        """

        handler_obj = AbstractDialoguePreProcessorHandlerFactory().get_dialogue_preprocessor_handler(
            StandardFlowDialoguePreProcessorHandlerImpl.__name__)
        return handler_obj.perform_preprocessing({
            AbstractDialoguePreProcessor.__name__: args[StandardFlowDialoguePreProcessorHandlerImpl.__name__],
            PandasDAOImpl.__name__: args[PandasDAOImpl.__name__]
        })

    def validation(self, args):
        if args is None:
            self.logger.error(MissingMandatoryFieldException.__name__, 'Given:', type(None))
            raise MissingMandatoryFieldException('Given:', type(None))
        if not isinstance(args, dict):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', type(dict))
            raise InvalidInfoException('Given:', type(args), 'Required:', type(dict))
        if StandardFlowDialoguePreProcessorHandlerImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(), 'Required:', StandardFlowDialoguePreProcessorHandlerImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(),
                                                 'Required:', StandardFlowDialoguePreProcessorHandlerImpl.__name__)
        if args[StandardFlowDialoguePreProcessorHandlerImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(list))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(list))
        if not isinstance(args[StandardFlowDialoguePreProcessorHandlerImpl.__name__], list):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args[StandardFlowDialoguePreProcessorHandlerImpl.__name__]),
                              'Required:', type(list))
            raise InvalidInfoException('Given:', type(args[StandardFlowDialoguePreProcessorHandlerImpl.__name__]),
                                       'Required:', type(list))
        for config in args[StandardFlowDialoguePreProcessorHandlerImpl.__name__]:
            if not isinstance(config, AbstractConfig):
                self.logger.error(InvalidInfoException.__name__,
                                  'Given:', type(config), 'Required:', type(AbstractConfig))
                raise InvalidInfoException('Given:', type(config), 'Required:', type(AbstractConfig))
        if PandasDAOImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
        if args[PandasDAOImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(pd.DataFrame))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(pd.DataFrame))
        return True
