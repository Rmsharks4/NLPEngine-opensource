"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects which implementation should be used at a given time:
- get_dialogue_handler_handler (pass in class name as argument)

"""

import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl
from preprocessing.bl.AbstractDialoguePreProcessorHandler import AbstractDialoguePreProcessingHandler
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException


class AbstractDialoguePreProcessorHandlerFactory:

    def __init__(self):
        """
        initializes Abstract Dialogue Pre-Processor Handler Factory
        """
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def get_dialogue_handler_handler(self, handler_type):

        # TRY THIS:
        try:

            # IF INITIAL VALIDATION SUCCESSFUL:
            if self.validation(handler_type):

                # GET REQUIRED HANDLER TYPE FROM DICT:
                switcher = dict()
                for y in AbstractDialoguePreProcessingHandler().__class__.__subclasses__():
                    switcher[y.__name__] = y()
                    switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))

                # RETURN HANDLER CLASS IF EXISTS:
                return switcher.get(handler_type, None)

        # CATCH ERRORS:
        except (MissingMandatoryFieldException, InvalidInfoException) as exp:
            raise CommonBaseException(exp)

    def validation(self, handler_type):

        # IF HANDLER_TYPE IS NONE:
        if handler_type is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', None, 'Required:', str)
            raise MissingMandatoryFieldException('Given:', None, 'Required:', str)

        # IF HANDLER_TYPE IS NOT STRING:
        if not isinstance(handler_type, str):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(handler_type), 'Required:', str)
            raise InvalidInfoException('Given:', type(handler_type), 'Required:', str)

        # IF HANDLER_TYPE NOT A CHILD OF ABSTRACT_DIALOGUE_HANDLER:
        if handler_type not in [y.__name__ for y in AbstractDialoguePreProcessingHandler().__class__.__subclasses__()]:
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', handler_type,
                              'Required Value from :', [y.__name__ for y in
                                                        AbstractDialoguePreProcessingHandler().__class__.__subclasses__()])
            raise InvalidInfoException('Given:', handler_type,
                                       'Required Value from :', [y.__name__ for y in
                                                                 AbstractDialoguePreProcessingHandler().__class__.__subclasses__()])

        # ALL CASES POSITIVE
        return True
