"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class follows the following flow of pre-processing (as visible in configurations)
- Lowercase
- Split Joint Words
- Contractions
- Numbers
- Email
- Punctuation
- Spell Check
- Stop Words
- Lemmatize

"""

from preprocessing.bl.AbstractDialoguePreProcessorHandler import AbstractDialoguePreProcessingHandler
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory
from preprocessing.utils.UtilsFactory import UtilsFactory


class StandardFlowDialoguePreProcessorHandlerImpl(AbstractDialoguePreProcessingHandler):

    def __init__(self):
        """
        initializes Standard Flow Dialogue Pre-Processor Handler Implementation Class
        """
        super().__init__()

    def perform_preprocessing(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (list) Abstract Config
        (list) Spark Data-frame
        """
        preprocessors = list()
        preprocessors.append(None)
        for current in args[AbstractDialoguePreProcessor.__name__]:
            while current.config_pattern.properties.req_data not in preprocessors:
                current = current.config_pattern.properties.req_data
            preprocessors.append(current)
        for current in reversed(preprocessors):
            df = []
            for data in args[current.config_pattern.properties.req_data]:
                df.append(AbstractDialoguePreProcessorFactory.get_dialogue_preprocessor(current).preprocess(
                    {
                        current.config_pattern.properties.req_data: data,
                        current.config_pattern.properties.req_args: UtilsFactory.get_utils(current.configconfig_pattern.properties.req_args)
                    }
                ))
            args[current.__name__] = df
        pass
