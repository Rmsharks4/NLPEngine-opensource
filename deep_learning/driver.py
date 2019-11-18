from commons.config.AbstractConfig import AbstractConfig
from preprocessing.bl import *
from feature_engineering.bl.acts import *
from feature_engineering.bl.steps import *
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl
from feature_engineering.bl.HoldTimeDialogueFeatureEngineerImpl import HoldTimeDialogueFeatureEngineerImpl
from feature_engineering.bl.NGramsDialogueFeatureEngineerImpl import NGramsDialogueFeatureEngineerImpl
from feature_engineering.bl.WordsPerMinuteDialogueFeatureEngineerImpl import WordsPerMinuteDialogueFeatureEngineerImpl
from preprocessing.driver.PreProcessorService import PreProcessorService
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from feature_engineering.driver.FeatureEngineeringService import FeatureEngineeringService
from commons.dao.PandasDAOImpl import PandasDAOImpl
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.StandardFlowDialogueFeatureEngineerHandlerImpl import StandardFlowDialogueFeatureEngineerHandlerImpl
from commons.dao.AbstractDAOFactory import AbstractDAOFactory
from vectorization.bl.StandardFlowVectorizerHandlerImpl import StandardFlowVectorizerHandlerImpl
from vectorization.driver.VectorizerService import VectorizerService


def run_preprocessor(configlist, dao_obj):
    service = PreProcessorService()
    print('PreProcessor Service running ...')
    return service.run({
        PandasDAOImpl.__name__: dao_obj,
        StandardFlowDialoguePreProcessorHandlerImpl.__name__: configlist
    })


def run_feature_engineer(configlist, dao_obj):
    service = FeatureEngineeringService()
    print('FeatureEngineer Service running ...')
    return service.run({
        PandasDAOImpl.__name__: dao_obj,
        StandardFlowDialogueFeatureEngineerHandlerImpl.__name__: configlist
    })


def run_vectorization(configlist, dao_obj):
    service = VectorizerService()
    print('Vectorizer Service running ...')
    return service.run({
        PandasDAOImpl.__name__: dao_obj,
        StandardFlowVectorizerHandlerImpl.__name__: configlist
    })


preconfiglist = dict()

var = StandardConfigParserImpl()
var.read_config('../../preprocessing/resources/' + AbstractDialoguePreProcessor.__name__ + '.ini')

for config in var.config_pattern.properties.children:
    configparser = StandardConfigParserImpl()
    configparser.read_config('../../preprocessing/resources/' + config + '.ini')
    preconfiglist[config] = configparser.config_pattern

feaconfiglist = dict()

var = StandardConfigParserImpl()
var.read_config('../../feature_engineering/resources/' + AbstractDialogueFeatureEngineer.__name__ + '.ini')

for config in var.config_pattern.properties.children:
    configparser = StandardConfigParserImpl()
    configparser.read_config('../../feature_engineering/resources/' + config + '.ini')
    feaconfiglist[config] = configparser.config_pattern

dao_obj = AbstractDAOFactory.get_dao(PandasDAOImpl.__name__)
data_obj = dao_obj.load(['../../data/input.csv', 'TempService'])
data_obj = run_preprocessor(preconfiglist, data_obj)
data_obj = run_feature_engineer(feaconfiglist, data_obj)



