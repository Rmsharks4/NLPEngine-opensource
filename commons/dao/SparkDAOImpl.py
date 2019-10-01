
from pyspark import SparkContext
from pyspark.sql import SparkSession
from commons.dao.AbstractDAO import AbstractDAO


class SparkDAOImpl(AbstractDAO):

    def __init__(self):
        super().__init__()
        self.spark = SparkSession.builder.getOrCreate()

    def load(self, args):
        df = self.spark.read.csv(args[0], header=True)
        df.createOrReplaceTempView(args[1])
        return df

    def create(self, args):
        df = self.spark.createDataFrame(args[0])
        df.createOrReplaceTempView(args[1])
        return df

    def save(self, args):
        args[0].toPandas().to_csv(args[1])

    def query(self, args):
        df = self.spark.sql(args[0])
        df.createOrReplaceTempView(args[1])
        return df

    def stop(self):
        self.spark.stop()
