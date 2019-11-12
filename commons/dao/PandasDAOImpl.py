from commons.dao.AbstractDAO import AbstractDAO
import pandas as pd


class PandasDAOImpl(AbstractDAO):

    def __init__(self):
        super().__init__()

    def load(self, args):
        df = pd.read_csv(args[0], sep=',', encoding='utf-8', skipinitialspace=True)
        return df

    def save(self, args):
        args[0].to_csv(args[1], index=None)
