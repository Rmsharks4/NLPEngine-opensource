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

        num_of_convs = labels_df['Call_Log'].count()
        print('Number', num_of_convs)

        features = ['SpeakerDataImpl', 'TokenTagsDialogueFeatureEngineerImpl', 'POSTagsDialogueFeatureEngineerImpl',
                    'NounChunkTagsFeatureEngineerImpl', 'NERTagsDialogueFeatureEngineerImpl',
                    'SynTagsDialogueFeatureEngineerImpl', 'AntoTagsDialogueFeatureEngineerImpl',
                    'DepTagsDialogueFeatureEngineerImpl', 'SentTagsDialogueFeatureEngineerImpl',
                    'IOBTagsDialogueFeatureEngineerImpl', 'CorefTagsDialogueFeatureEngineerImpl',
                    'HoldTimeDialogueFeatureEngineerImpl', 'WordsPerMinuteDialogueFeatureEngineerImpl',
                    'BackwardStepsDialogueFeatureEngineerImpl', 'QWhDialogueActImpl',
                    'QYnDialogueActImpl', 'ForwardStepsDialogueFeatureEngineerImpl',
                    'DaleChallaDifficultyIndexDialogueFeatureEngineerImpl']

        summ = 0
        maxi = 0

        # print(train_df.columns)

        train_data = []

        for row in labels_df.values:
            rows = train_df.where(train_df['ConversationIDDataImpl'] == str(row[0]))
            rows = rows.dropna()
            if len(rows) > maxi:
                maxi = len(rows)
            summ += len(rows)
            train_data.append([[row[1],  # SPEAKER
                                row[13],  # TOKENS
                                row[15],  # WPM
                                row[16],  # HOLD TIME
                                # row[67],  # ANTO
                                row[67],  # COREF
                                row[68],  # DEP
                                row[69],  # IOB
                                row[70],  # NER
                                row[71],  # NOUN
                                row[72],  # POS
                                row[73],  # SENT
                                # row[75],  # SYN
                                row[74],  # DALE CHALLA
                                row[79],  # QWH
                                row[80],  # QYN
                                row[81],  # BACK STEPS
                                row[82]  # FORW STEPS
                                ] for row in rows.values])

        avg = summ / num_of_convs

        print('Average', avg)
        print('Maxximum', maxi)

        # print(train_data)

        input_shape = (num_of_convs, avg, len(features))

        # input shape: 113, 46, 18

        # Vectorize Data Now!

        def numpy_fillna(data):
            data = np.array([np.array(i).reshape(1) for i in data])
            # Get lengths of each row of data
            lens = np.array([len(i) for i in data])
            # Mask of valid places in each row
            mask = np.arange(lens.max()) < lens[:, None]
            # Setup output array and put elements from data into masked positions
            out = np.zeros(mask.shape, dtype=data.dtype)
            out[mask] = np.concatenate(data)
            return out

        def numpy_fillnan(data):
            # Get lengths of each row of data
            lens = np.array([len(i) for i in data])
            # Mask of valid places in each row
            mask = np.arange(lens.max()) < lens[:, None]
            # Setup output array and put elements from data into masked positions
            out = np.zeros(mask.shape, dtype=data.dtype)
            out[mask] = np.concatenate(data)
            return out

        @nb.jit()
        def f(a):
            print('len')
            l = len(max(a, key=len))
            print('empty')
            a0 = np.empty(a.shape + (l,))
            print('enumerate')
            for n, i in enumerate(a):
                a0[n] = np.pad(i, (0, l - len(i)), mode='constant')
            a = a0
            return a

        # data = np.asarray([np.pad(r, (0, maxi - len(r)), 'constant', constant_values=0) for r in train_data])

        for row in train_data:
            for data in row:
                print('Features', numpy_fillna(np.asarray(data)).shape)

        print('Conversations', f(np.asarray(train_data)).shape)

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

