
from preprocessing.bl.AbstractDialoguePreProcessorHandler import AbstractDialoguePreProcessingHandler
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory
from preprocessing.utils.UtilsFactory import UtilsFactory


class StandardFlowDialoguePreProcessorHandlerImpl(AbstractDialoguePreProcessingHandler):

    def __init__(self):
        super().__init__()

    def perform_preprocessing(self, args):
        preprocessors = list()
        preprocessors.append(None)
        for current in args[AbstractDialoguePreProcessor.__class__.__name__]:
            while current.config_pattern.properties.req_data not in preprocessors:
                current = current.config_pattern.properties.req_data
            preprocessors.append(current)
        # assume it is now sorted
        for current in reversed(preprocessors):
            df = []
            for data in args[current.config_pattern.properties.req_data]:
                df.append(AbstractDialoguePreProcessorFactory.get_dialogue_preprocessor(current).preprocess(
                    {
                        current.config_pattern.properties.req_data: data,
                        current.config_pattern.properties.req_args: UtilsFactory.get_utils(current.configconfig_pattern.properties.req_args)
                    }
                ))
            args[current.__class__.__name__] = df
        pass
