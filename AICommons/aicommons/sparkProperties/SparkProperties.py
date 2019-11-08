"""
Authors: sfatima@i2cinc.com

Purpose:
This file contains a database connection class that allows to group database connection parameters for python


"""
from pyspark import SQLContext


class SparkProperties:
    def __init__(self, url, properties=None, spark=None, sc=None):
        self.sql_context = SQLContext(sc)
        self.url = url
        self.properties = properties
        self.spark = spark
        self.sc = sc

