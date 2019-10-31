from feature_engineering.utils.UtilsFactory import UtilsFactory
from feature_engineering.bl.AbstractDialogueFeatureEngineerHandler import AbstractDialogueFeatureEngineerHandler
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.AbstractDialogueFeatureEngineerFactory import AbstractDialogueFeatureEngineerFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl


class StandardFlowDialogueFeatureEngineerHandlerImpl(AbstractDialogueFeatureEngineerHandler):

    def __init__(self):
        """
        initializes Standard Flow Dialogue Pre-Processor Handler Implementation Class
        """
        super().__init__()

    def perform_feature_engineering(self, args):
        engineers = list()

        # Arranging configs in order of execution!
        for current in args[AbstractDialogueFeatureEngineer.__name__].values():
            if current.properties.req_data is not None:
                for datalist in current.properties.req_data:
                    for data in datalist:
                        print(current.name)
                        while data not in engineers:
                            current = args[AbstractDialogueFeatureEngineer.__name__][current.properties.data]
                        if current.name not in engineers:
                                engineers.append(current.name)
            else:
                engineers.append(current.name)

        spark = SparkDAOImpl()
        spark_df = args[SparkDAOImpl.__name__]
        df = spark_df.toPandas()
        prev = ''

        for eng in engineers:

            print(eng)

            engineer = AbstractDialogueFeatureEngineerFactory.get_feature_engineer(eng)
            input_data = []

            if engineer.config_pattern.properties.req_input is not None:
                input_data.extend(engineer.config_pattern.properties.req_input)
            if engineer.config_pattern.properties.req_data is not None:
                input_data.extend(engineer.config_pattern.properties.req_data)

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
                        if names[0] == elem:
                            elem_types.append('.'.join(names))
                    elements.append([(elem, etypes) for etypes in elem_types])

                # print(eng, elements)

                combos = StandardFlowDialogueFeatureEngineerHandlerImpl.combine(elements)

                # print(eng, combos)

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

                    dfargs[engineer.config_pattern.properties.req_args] = util

                    # print('Cols', cols)

                    # print('Dfargs', [(dfargname, dfargval) for dfargname, dfargval in dfargs.items()])

                    colname = ''

                    if len(cols) > 0:
                        colname = eng + '.' + '.'.join(e for e in cols)
                    else:
                        colname = eng

                    df[colname] = \
                        df[cols].apply(lambda x: engineer.engineer_feature_operation(
                            dict((dfargname, x) if x.name == dfargval else (dfargname, dfargval)
                                 for dfargname, dfargval in dfargs.items())))

                    print(df[colname].head(), '\n')

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
            while next >= 0 and (indices[next] + 1 >= len(arr[next])):
                next -= 1
            if next < 0:
                return combos
            indices[next] += 1
            for i in range(next + 1, n):
                indices[i] = 0
