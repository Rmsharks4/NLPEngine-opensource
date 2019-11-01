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
            if current.properties.req_data is not None:
                for datalist in current.properties.req_data:
                    for data in datalist:
                        while data not in preprocessors:
                            current = args[AbstractDialoguePreProcessor.__name__][data]
                        if current.name not in preprocessors:
                            preprocessors.append(current.name)
            else:
                preprocessors.append(current.name)
        spark = SparkDAOImpl()
        spark_df = args[SparkDAOImpl.__name__]
        df = spark_df.toPandas()

        for pre in preprocessors:
            preprocessor = AbstractDialoguePreProcessorFactory.get_dialogue_preprocessor(pre)
            input_data = []

            if preprocessor.config_pattern.properties.req_input is not None:
                input_data.extend(preprocessor.config_pattern.properties.req_input)
            if preprocessor.config_pattern.properties.req_data is not None:
                input_data.extend(preprocessor.config_pattern.properties.req_data)

            util = UtilsFactory.get_utils(preprocessor.config_pattern.properties.req_args)
            if util is not None:
                util.load()

            for req_data in input_data:
                elements = []

                for elem in req_data:
                    input_df = df.filter(regex=elem)

                    elem_types = []
                    for col in input_df.columns:
                        names = col.split('.')
                        if names[0] == elem:
                            elem_types.append('.'.join(names))
                    elements.append([(elem, etypes) for etypes in elem_types])

                combos = StandardFlowDialoguePreProcessorHandlerImpl.combine(elements)

                for elem in combos:
                    dfargs = dict()
                    cols = []
                    if type(elem) is list:
                        for e in elem:
                            dfargs[e[0]] = e[1]
                            cols.append(e[1])
                    else:
                        dfargs[elem[0]] = elem[1]
                        cols.append(elem[1])

                    dfargs[preprocessor.config_pattern.properties.req_args] = util

                    if len(cols) > 0 and len(input_data) > 1:
                        colname = pre + '.' + '.'.join(e for e in cols)
                    else:
                        colname = pre

                    df[colname] = \
                        df[cols].apply(lambda x: preprocessor.preprocess_operation(
                            dict((dfargname, x) if x.name == dfargval else (dfargname, dfargval)
                                 for dfargname, dfargval in dfargs.items())))

        return spark.create([
            df, self.__class__.__name__
        ])

    @staticmethod
    def combine(arr):
        n = len(arr)
        indices = [0 for i in range(n)]
        combos = []
        while 1:
            for i in range(n):
                combos.append(arr[i][indices[i]])
            next = n - 1
            while next >= 0 and (indices[next] + 1 >= len(arr[next])):
                next -= 1
            if next < 0:
                return combos
            indices[next] += 1
            for i in range(next + 1, n):
                indices[i] = 0
