"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects which implementation should be used at a given time:
- get_dialogue_preprocessor_handler (pass in class name as argument)

"""

from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl


class AbstractDialoguePreProcessorHandlerFactory:

    @staticmethod
    def get_dialogue_preprocessor_handler(handler_type):
        switcher = {
            StandardFlowDialoguePreProcessorHandlerImpl.__name__: StandardFlowDialoguePreProcessorHandlerImpl()
        }
        return switcher.get(handler_type, None)
