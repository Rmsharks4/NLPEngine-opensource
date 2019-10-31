from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from feature_engineering.driver.FeatureEngineeringService import FeatureEngineeringService
from commons.dao.SparkDAOImpl import SparkDAOImpl
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.AbstractConversationFeatureEngineer import AbstractConversationFeatureEngineer
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl
from feature_engineering.bl.StandardFlowConversationFeatureEngineerHandlerImpl import StandardFlowConversationFeatureEngineerHandlerImpl
from preprocessing.bl import *
from feature_engineering.bl.acts import *
from feature_engineering.bl.steps import *
from feature_engineering.bl.HoldTimeConversationFeatureEngineerImpl import HoldTimeDialogueFeatureEngineer
from feature_engineering.bl.NGramsDialogueFeatureEngineerImpl import NGramsDialogueFeatureEngineerImpl
from feature_engineering.bl.WordsPerMinuteDialogueFeatureEngineerImpl import WordsPerMinuteDialogueFeatureEngineerImpl

# abc = AbstractDialogueFeatureEngineer().parse()
#
# for y in AbstractDialogueFeatureEngineer().__class__.__subclasses__():
#     y().parse()
#     [x().parse() for x in y().__class__.__subclasses__()]
#
#
# abc = AbstractConversationFeatureEngineer().parse()
#
# for y in AbstractConversationFeatureEngineer().__class__.__subclasses__():
#     y().parse()
#     [x().parse() for x in y().__class__.__subclasses__()]

var = StandardConfigParserImpl()
var.read_config('resources/'+AbstractDialogueFeatureEngineer.__name__+'.ini')

configlistdial = dict()

for config in var.config_pattern.properties.children:
    configparser = StandardConfigParserImpl()
    configparser.read_config('resources/'+config+'.ini')
    configlistdial[config] = configparser.config_pattern

var = StandardConfigParserImpl()
var.read_config('resources/'+AbstractConversationFeatureEngineer.__name__+'.ini')

configlistconv = dict()

for config in var.config_pattern.properties.children:
    configparser = StandardConfigParserImpl()
    configparser.read_config('resources/'+config+'.ini')
    configlistconv[config] = configparser.config_pattern

service = FeatureEngineeringService()
service.run({
    SparkDAOImpl.__name__: '../data/'+FeatureEngineeringService.__name__+'.csv',
    StandardFlowDialogueFeatureEngineerHandlerImpl.__name__: configlistdial,
    StandardFlowConversationFeatureEngineerHandlerImpl.__name__: configlistconv
})
