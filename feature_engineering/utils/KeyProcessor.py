from flashtext.keyword import KeywordProcessor
import csv
from feature_engineering.utils.AbstractUtils import AbstractUtils


class KeyProcessor(AbstractUtils):

    kp = None
    file = None

    @staticmethod
    def load():
        if KeyProcessor.file is not None:
            KeyProcessor.kp = KeywordProcessor()
            with open('../data/intents/'+KeyProcessor.file+'.csv', mode='r') as infile:
                reader = csv.reader(infile)
                for row in reader:
                    KeyProcessor.kp.add_keyword(row[0], row[1])

    @staticmethod
    def set_filename(name):
        KeyProcessor.file = name
        KeyProcessor.load()
