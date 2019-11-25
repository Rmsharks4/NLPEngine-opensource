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
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from deep_learning.bl.models.TFDeepLearningModelImpl import TFDeepLearningModelImpl
from AIModelTrain.aimodeltrain.driver.AbstractTrainDriverFactory import AbstractTrainDriverFactory
from AIModelTrain.aimodeltrain.driver.ModelTrainDriver import ModelTrainDriver

from keras import backend as K
import keras.layers as layers
from keras.models import Model, load_model
from keras.engine import Layer
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import nltk
from nltk.corpus import wordnet
import numpy as np
import numba as nb
import warnings
from sklearn.model_selection import train_test_split


def warn(*args, **kwargs):
    pass


warnings.warn = warn
warnings.filterwarnings("ignore")



class TempService:

    def run(self):
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

        feaconfiglist.pop('AntoTagsDialogueFeatureEngineerImpl')
        feaconfiglist.pop('SynTagsDialogueFeatureEngineerImpl')

        dao_obj = AbstractDAOFactory.get_dao(PandasDAOImpl.__name__)
        data_obj = dao_obj.load(['../../data/input.csv', TempService.__name__])
        data_obj = TempService.run_preprocessor(preconfiglist, data_obj)
        data_obj = TempService.run_feature_engineer(feaconfiglist, data_obj)

        train_df = data_obj
        labels_df = pd.read_csv('../../data/allabels.csv', encoding='latin1')

        final = list()

        for row in labels_df.values:
            rows = train_df.where(train_df['ConversationIDDataImpl'] == str(row[0]))
            rows = rows.dropna()
            for val in rows.values:
                final.append([row[0], str(val[4]), row[15]])

        mid_df = pd.DataFrame(final, index=None, columns=['ConversationIDDataImpl', 'PlainTextDataImpl',
                                                          'Actively_listened_and_acknowledged_concerns'])

        train, test = train_test_split(mid_df, test_size=0.2)

        abs_train_driver_factory = AbstractTrainDriverFactory()

        train_driver_inst_naive_bayes = abs_train_driver_factory.get_instance("naive_bayes")

        myparam = {
            CommonConstants.MODEL_OUTPUT_DIR: '/results/MY_BERT',
            CommonConstants.SAVE_SUMMARY_STEPS: 100,
            CommonConstants.SAVE_CHECKPOINTS_STEPS: 10000,
            CommonConstants.BERT_MODEL_HUB: "https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1",
            CommonConstants.LEARNING_RATE: 2e-5,
            CommonConstants.NUM_TRAIN_EPOCHS: 1.0,
            CommonConstants.TEST_OR_TRAIN: 0,
            CommonConstants.BATCH_SIZE: 64,
            CommonConstants.READ_DATA_COLUMNS_TAG: "PlainTextDataImpl",
            CommonConstants.LABEL_COLUMN_TAG: "Actively_listened_and_acknowledged_concerns",
            CommonConstants.MAX_SEQ_LENGTH: 128,
            CommonConstants.WARMUP_PROPORTION: 0.1
        }

        myparam[CommonConstants.NUM_TRAIN_STEPS] = int(len(train) / myparam[CommonConstants.BATCH_SIZE] * myparam[CommonConstants.NUM_TRAIN_EPOCHS])
        myparam[CommonConstants.NUM_WARM_STEPS] = int(myparam[CommonConstants.NUM_TRAIN_STEPS] * myparam[CommonConstants.WARMUP_PROPORTION])
        myparam[CommonConstants.CLASS_LABEL] = train[myparam[CommonConstants.LABEL_COLUMN_TAG]].unique().tolist()

        model_params = {
            "model_name": TFDeepLearningModelImpl.__name__,
            "enable_cv": "N",
            "feature_list": list(myparam[CommonConstants.READ_DATA_COLUMNS_TAG]),
            "targetCol": myparam[CommonConstants.LABEL_COLUMN_TAG]
        }

        model_hyper_params = myparam

        model_cross_validator_params = {}

        model = train_driver_inst_naive_bayes.train_model(data=train, target=None, model_params=model_params,
                                                          model_hyper_params=model_hyper_params,
                                                          model_cross_validator_params=model_cross_validator_params)

        result, model = TFDeepLearningModelImpl().test(model, test, None, myparam)

        redf = pd.DataFrame([result]).T
        redf.columns = ["values"]

        print(redf)

    @staticmethod
    def run_preprocessor(configlist, dao_obj):
        service = PreProcessorService()
        print('PreProcessor Service running ...')
        return service.run({
            PandasDAOImpl.__name__: dao_obj,
            StandardFlowDialoguePreProcessorHandlerImpl.__name__: configlist
        })

    @staticmethod
    def run_feature_engineer(configlist, dao_obj):
        service = FeatureEngineeringService()
        print('FeatureEngineer Service running ...')
        return service.run({
            PandasDAOImpl.__name__: dao_obj,
            StandardFlowDialogueFeatureEngineerHandlerImpl.__name__: configlist
        })

    @staticmethod
    def run_vectorization(args):
        pass

    @staticmethod
    def run_model_training(args):
        pass

    @staticmethod
    def run_model_testing(args):
        pass

    @staticmethod
    def run_model_evaluation(args):
        pass


if __name__ == '__main__':
    service = TempService()
    service.run()

