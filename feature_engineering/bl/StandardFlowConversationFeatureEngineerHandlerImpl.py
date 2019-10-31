from feature_engineering.utils.UtilsFactory import UtilsFactory
from feature_engineering.bl.AbstractConversationFeatureEngineerHandler import AbstractConversationFeatureEngineerHandler
from feature_engineering.bl.AbstractConversationFeatureEngineer import AbstractConversationFeatureEngineer
from feature_engineering.bl.AbstractConversationFeatureEngineerFactory import AbstractConversationFeatureEngineerFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl


class StandardFlowConversationFeatureEngineerHandlerImpl(AbstractConversationFeatureEngineerHandler):

    def __init__(self):
        """
        initializes Standard Flow Dialogue Pre-Processor Handler Implementation Class
        """
        super().__init__()

    def perform_feature_engineering(self, args):
        engineers = list()

        for current in args[AbstractConversationFeatureEngineer.__name__].values():
            if len(current.properties.req_data) > 0:
                for data in current.properties.req_data:
                    while data not in engineers:
                        current = args[AbstractConversationFeatureEngineer.__name__][data]
                    if current.name not in engineers:
                        engineers.append(current.name)
            else:
                engineers.append(current.name)

        spark = SparkDAOImpl()
        spark_df = args[SparkDAOImpl.__name__]
        df = spark_df.toPandas()
        prev = ''

        for eng in engineers:
            engineer = AbstractConversationFeatureEngineerFactory.get_feature_engineer(eng)
            input_data = engineer.config_pattern.properties.req_data

            util = UtilsFactory.get_utils(engineer.config_pattern.properties.req_args)
            if util is not None:
                util.load()

            for req_data in input_data:
                elements = []

                for elem in req_data:
                    input_df = df.filter(regex=elem)
                    elem_types = []
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
                        elem_types.append(names)
                    elements.append(elem_types)

                combos = StandardFlowConversationFeatureEngineerHandlerImpl.combine(elements)

                for elem in combos:
                    dfargs = dict()
                    for data in req_data:
                        dfargs[data] = ''.join(e if data in e else None for e in elem)
                    dfargs.update([engineer.config_pattern.properties.req_args, util])
                    df[engineer.__class__.__name__ + '.'.join(e for e in elem)] = engineer.engineer_feature(
                        dict((dfargname, df[dfargval]) for dfargname, dfargval in dfargs.items()))

            prev = eng

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
            while (next >= 0 and
                   (indices[next] + 1 >= len(arr[next]))):
                next -= 1
            if next < 0:
                return combos
            indices[next] += 1
            for i in range(next + 1, n):
                indices[i] = 0
