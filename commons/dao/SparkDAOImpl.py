from pyspark import SparkContext
from pyspark.sql import SparkSession
from commons.dao.AbstractDAO import AbstractDAO
import pandas as pd

# Maha asked to change to Pandas so need to do thaattt

class SparkDAOImpl(AbstractDAO):

    def __init__(self):
        super().__init__()
        self.spark = SparkSession.builder.getOrCreate()

    def load(self, args):
        df = pd.read_csv(args[0], sep=',', encoding='utf-8', skipinitialspace=True)
        return df

    def create(self, args):
        df = self.spark.createDataFrame(args[0])
        df.createOrReplaceTempView(args[1])
        return df

    def save(self, args):
        args[0].toPandas().to_csv(args[1], index=None)

    def query(self, args):
        df = self.spark.sql(args[0])
        df.createOrReplaceTempView(args[1])
        return df

    def stop(self):
        self.spark.stop()
