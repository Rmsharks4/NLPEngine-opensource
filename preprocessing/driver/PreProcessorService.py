"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class contains a 'run' function that runs the whole routine - starting from DAO to BL to DAO again.
- An implementation of **Abstract Service** in NLP.commons
- Implements the following main function: **run**

"""

import logging
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from commons.dao.PandasDAOImpl import PandasDAOImpl
from preprocessing.bl.AbstractDialoguePreProcessorHandlerFactory import AbstractDialoguePreProcessorHandlerFactory
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl


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

        handler_obj = AbstractDialoguePreProcessorHandlerFactory.get_dialogue_preprocessor_handler(StandardFlowDialoguePreProcessorHandlerImpl.__name__)
        return handler_obj.perform_preprocessing({
            AbstractDialoguePreProcessor.__name__: args[StandardFlowDialoguePreProcessorHandlerImpl.__name__],
            PandasDAOImpl.__name__: args[PandasDAOImpl.__name__]
        })
