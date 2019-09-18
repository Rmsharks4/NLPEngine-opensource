from preprocessing.bl.LinkedList import LinkedList
from commons.config.AbstractConfig import AbstractConfig
from commons.config.AbstractConfigParser import AbstractConfigParser

class VectorizerService:

    def main(self):
        configlist = LinkedList(AbstractConfig)
        CONFIG_FILE = 'Vectorization.yml'
        # config parser will take 2 elements: the class and its encoding - for every class, call its list of encodings!
        config_parser = AbstractConfigParser()
        config_parser.read(CONFIG_FILE)
        config_parser.parse(configlist)
        # now it should fill the list with connections of all the things inside every config!

