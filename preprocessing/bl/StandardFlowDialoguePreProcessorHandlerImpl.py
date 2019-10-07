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
from commons.dao.SparkDAOImpl import SparkDAOImpl


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
        for current in args[AbstractDialoguePreProcessor.__name__].values():
            if type(current.properties.req_data) == list:
                for data in current.properties.req_data:
                    while data is not None and data not in preprocessors:
                        current = args[AbstractDialoguePreProcessor.__name__][data]
                    preprocessors.append(current.name)
            else:
                while current.properties.req_data is not None and current.properties.req_data not in preprocessors:
                    current = args[AbstractDialoguePreProcessor.__name__][current.properties.req_data]
                preprocessors.append(current.name)
        spark = SparkDAOImpl()
        spark_df = args[SparkDAOImpl.__name__]
        df = spark_df.toPandas()
        for name in preprocessors:
            preprocessor = AbstractDialoguePreProcessorFactory.get_dialogue_preprocessor(name)
            if type(preprocessor.config_pattern.properties.req_data) == list:
                for req_data in preprocessor.config_pattern.properties.req_data:
                    util = UtilsFactory.get_utils(preprocessor.config_pattern.properties.req_args)
                    if util is not None:
                        util.load()
                    df[preprocessor.__class__.__name__+'_'+req_data] = df[req_data] \
                        .apply(lambda x: preprocessor.preprocess_operation({
                            req_data: x,
                            preprocessor.config_pattern.properties.req_args: util
                        }) if x is not None else x)
            else:
                util = UtilsFactory.get_utils(preprocessor.config_pattern.properties.req_args)
                if util is not None:
                    util.load()
                df[preprocessor.__class__.__name__] = df[preprocessor.config_pattern.properties.req_data]\
                    .apply(lambda x: preprocessor.preprocess_operation({
                        preprocessor.config_pattern.properties.req_data: x,
                        preprocessor.config_pattern.properties.req_args: util
                    }) if x is not None else x)
        return spark.create([
            df, self.__class__.__name__
        ])
