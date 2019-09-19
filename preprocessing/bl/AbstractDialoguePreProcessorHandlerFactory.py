
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl


class AbstractDialoguePreProcessorHandlerFactory:

    @staticmethod
    def get_dialogue_preprocessor_handler(handler_type):
        switcher = {
            StandardFlowDialoguePreProcessorHandlerImpl.__class__.__name__: StandardFlowDialoguePreProcessorHandlerImpl()
        }
        return switcher.get(handler_type, None)
