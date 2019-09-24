"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects which implementation should be used at a given time:
- get_dialogue_preprocessor_handler (pass in class name as argument)

"""

import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl


class AbstractDialoguePreProcessorHandlerFactory:

    def __init__(self):
        """
        initializes Abstract Dialogue Pre-Processor Handler Factory
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @staticmethod
    def get_dialogue_preprocessor_handler(handler_type):
        """

        :param handler_type: (str) AbstractDialoguePreProcessorHandlerImpl Class Name
        :return: (AbstractDialoguePreProcessorHandler) else throws Exception
        """
        switcher = {
            StandardFlowDialoguePreProcessorHandlerImpl.__name__: StandardFlowDialoguePreProcessorHandlerImpl()
        }
        return switcher.get(handler_type, None)
