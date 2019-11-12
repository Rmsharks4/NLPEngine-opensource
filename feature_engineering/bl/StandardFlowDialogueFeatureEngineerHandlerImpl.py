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

from feature_engineering.bl.AbstractDialogueFeatureEngineerHandler import AbstractDialogueFeatureEngineerHandler
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.AbstractDialogueFeatureEngineerFactory import AbstractDialogueFeatureEngineerFactory
from feature_engineering.utils.UtilsFactory import UtilsFactory
from commons.dao.PandasDAOImpl import PandasDAOImpl


class StandardFlowDialogueFeatureEngineerHandlerImpl(AbstractDialogueFeatureEngineerHandler):

    def __init__(self):
        """
        initializes Standard Flow Dialogue Pre-Processor Handler Implementation Class
        """
        super().__init__()

    @staticmethod
    def check_dep(args, current, engineers, stack):
        if current.properties.req_data is not None:
            for datalist in current.properties.req_data:
                for data in datalist:
                    temp = current
                    prev = current
                    while data is not None and data not in engineers:
                        stack.append(temp)
                        temp = StandardFlowDialogueFeatureEngineerHandlerImpl. \
                            check_dep(args, args[data], engineers, stack)
                        if temp is None or temp == prev:
                            return prev
                        prev = temp
                        data = temp.name
                    stack.append(temp)
                    return temp
        else:
            stack.append(current)
            return current

    def perform_feature_engineering(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (list) Abstract Config
        (list) Spark Data-frame
        """
        engineers = list()

        for current in args[AbstractDialogueFeatureEngineer.__name__].values():
            stack = []
            StandardFlowDialogueFeatureEngineerHandlerImpl\
                .check_dep(args[AbstractDialogueFeatureEngineer.__name__], current, engineers, stack)
            for s in reversed(stack):
                if s.name not in engineers:
                    engineers.append(s.name)

        df = args[PandasDAOImpl.__name__]

        for eng in engineers:

            print('Feature: ', eng, 'running ...')

            engineer = AbstractDialogueFeatureEngineerFactory.get_feature_engineer(eng)
            input_data = []

            if engineer.config_pattern.properties.req_input is not None:
                input_data.extend(engineer.config_pattern.properties.req_input)
            if engineer.config_pattern.properties.req_data is not None:
                input_data.extend(engineer.config_pattern.properties.req_data)

            util = UtilsFactory.get_utils(engineer.config_pattern.properties.req_args)
            if util is not None:
                util.load()

            elements = []

            for req_data in input_data:

                for elem in req_data:

                    input_df = df.filter(regex=elem)

                    elem_types = []
                    for col in input_df.columns:
                        names = col.split('.')
                        if names[0] == elem:
                            elem_types.append('.'.join(names))
                    elements.append([(elem, etypes) for etypes in elem_types])

            dfargs = dict()
            cols = []

            for elem in elements:
                if type(elem) is list:
                    for e in elem:
                        dfargs[e[0]] = e[1]
                        cols.append(e[1])
                else:
                    dfargs[elem[0]] = elem[1]
                    cols.append(elem[1])

            dfargs[engineer.config_pattern.properties.req_args] = util

            if len(cols) > 0 and len(input_data) > 1:
                colname = eng + '.' + '.'.join(e for e in cols)
            else:
                colname = eng

            for key in dfargs.keys():
                if key in df.columns:
                    dfargs[key] = df[key]

            df[colname] = engineer.engineer_feature_operation(dfargs)

        for col in df.columns:
            df[col] = df[col].apply(lambda x: str(x))
        return df

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
