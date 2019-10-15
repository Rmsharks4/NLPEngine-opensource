#
# from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
# from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
# from preprocessing.bl.PorterStemmerDialoguePreProcessorImpl import PorterStemmerDialoguePreProcessorImpl
# from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl
# from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl
# from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
# from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
# from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
# from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsPreProcessorImpl
# from preprocessing.bl.WordNetLemmatizerDialoguePreProcessorImpl import WordNetLemmatizerDialoguePreProcessorImpl
# from preprocessing.bl.PlainTextDialoguePreProcessorImpl import PlainTextDialoguePreProcessorImpl
# from commons.config.AbstractConfig import AbstractConfig
# from commons.config.AbstractConfigParser import AbstractConfigParser
#
# var = PlainTextDialoguePreProcessorImpl()
# var.parse()
#
# var = ExpandContractionsDialoguePreProcessorImpl()
# var.parse()
#
# var = LowercaseDialoguePreProcessorImpl()
# var.parse()
#
# var = PorterStemmerDialoguePreProcessorImpl()
# var.parse()
#
# var = RemoveEmailsDialoguePreProcessorImpl()
# var.parse()
#
# var = RemoveNumericCharactersDialoguePreProcessorImpl()
# var.parse()
#
# var = RemovePunctuationDialoguePreProcessorImpl()
# var.parse()
#
# var = RemoveStopWordsDialoguePreProcessorImpl()
# var.parse()
#
# var = SpellCheckerDialoguePreProcessorImpl()
# var.parse()
#
# var = SplitJointWordsPreProcessorImpl()
# var.parse()
#
# var = WordNetLemmatizerDialoguePreProcessorImpl()
# var.parse()


from preprocessing.driver.PreProcessorService import PreProcessorService
from commons.dao.SparkDAOImpl import SparkDAOImpl
from commons.config.AbstractConfig import AbstractConfig
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.PlainTextDialoguePreProcessorImpl import PlainTextDialoguePreProcessorImpl
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl
from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory

configlist = dict()

var = StandardConfigParserImpl()
var.read_config('resources/'+AbstractDialoguePreProcessor.__name__+'.ini')

for config in var.config_pattern.properties.children:
    configparser = StandardConfigParserImpl()
    configparser.read_config('resources/'+config+'.ini')
    configlist[config] = configparser.config_pattern

service = PreProcessorService()
service.run({
    SparkDAOImpl.__name__: '../data/'+AbstractDialoguePreProcessor.__name__+'.csv',
    StandardFlowDialoguePreProcessorHandlerImpl.__name__: configlist
})
