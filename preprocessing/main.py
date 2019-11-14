# from preprocessing.bl import *
# from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
#
# var = AbstractDialoguePreProcessor()
# var.parse()
#
# for y in var.__class__.__subclasses__():
#     y().parse()
#     [x().parse() for x in y().__class__.__subclasses__()]


from preprocessing.driver.PreProcessorService import PreProcessorService
from commons.dao.PandasDAOImpl import PandasDAOImpl
from commons.config.AbstractConfig import AbstractConfig
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl
from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory

# configlist = dict()
#
# var = StandardConfigParserImpl()
# var.read_config('resources/'+AbstractDialoguePreProcessor.__name__+'.ini')
#
# for config in var.config_pattern.properties.children:
#     configparser = StandardConfigParserImpl()
#     configparser.read_config('resources/'+config+'.ini')
#     configlist[config] = configparser.config_pattern
#
# service = PreProcessorService()
# service.run({
#     PandasDAOImpl.__name__: '../../data/' + AbstractDialoguePreProcessor.__name__ + '.csv',
#     StandardFlowDialoguePreProcessorHandlerImpl.__name__: configlist
# })

from preprocessing.utils.EmailsDictionary import EmailsDictionary
import pandas as pd

e = EmailsDictionary()
print(EmailsDictionary)
