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
import math


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
            if len(current.properties.req_data) > 0:
                for data in current.properties.req_data:
                    while data not in preprocessors:
                        current = args[AbstractDialoguePreProcessor.__name__][data]
                    if current.name not in preprocessors:
                        preprocessors.append(current.name)
            else:
                preprocessors.append(current.name)
        spark = SparkDAOImpl()
        spark_df = args[SparkDAOImpl.__name__]
        df = spark_df.toPandas()
        prev = ''
        for pre in preprocessors:
            preprocessor = AbstractDialoguePreProcessorFactory.get_dialogue_preprocessor(pre)
            input_data = preprocessor.config_pattern.properties.req_data
            for req_data in input_data:
                util = UtilsFactory.get_utils(preprocessor.config_pattern.properties.req_args)
                if util is not None:
                    util.load()
                input_df = df.filter(regex=req_data)
                for col in input_df.columns:
                    names = col.split('.')
                    if names[0] == req_data:
                        if len(input_data) > 1:
                            if req_data == prev:
                                names.pop(0)
                            if len(names) > 0:
                                names[0] = '.' + names[0]
                        else:
                            names[0] = ''
                        df[preprocessor.__class__.__name__+'.'.join(names)] = df[col]\
                            .apply(lambda x: preprocessor.preprocess_operation({
                                req_data: x,
                                preprocessor.config_pattern.properties.req_args: util
                            }) if x is not None else x)
            prev = pre
        return spark.create([
            df, self.__class__.__name__
        ])

# PlainTextDialoguePreProcessorImpl - 1 dep
# LowercaseDialoguePreProcessorImpl - 1 dep (ignore appending)
# SplitJointWordsPreProcessorImpl - 2 deps (append in 2-1 dep)
# SplitJointWordsPreProcessorImpl.LowercaseDialoguePreProcessorImpl (append name of dep)
# ExpandContractionsDialoguePreProcessorImpl - 2 deps (append in 2-1 dep)
# ExpandContractionsDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl (append name of dep's dep)
# RemoveNumericCharactersDialoguePreProcessorImpl
# RemoveNumericCharactersDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# RemoveEmailsDialoguePreProcessorImpl
# RemoveEmailsDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# RemovePunctuationDialoguePreProcessorImpl
# RemovePunctuationDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# SpellCheckerDialoguePreProcessorImpl
# SpellCheckerDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# RemoveStopWordsDialoguePreProcessorImpl
# RemoveStopWordsDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# PorterStemmerDialoguePreProcessorImpl
# PorterStemmerDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# PorterStemmerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl
# PorterStemmerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# WordNetLemmatizerDialoguePreProcessorImpl
# WordNetLemmatizerDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
# WordNetLemmatizerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl
# WordNetLemmatizerDialoguePreProcessorImpl.SpellCheckerDialoguePreProcessorImpl.LowercaseDialoguePreProcessorImpl
