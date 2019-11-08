"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an implementation of abstract machine learning model class, it is meant to create and handle model
specific operations for Naive Bayes.

Class Functions:
_init_
load_from_HDFS

"""

import logging

from sklearn.naive_bayes import MultinomialNB

from AICommons.aicommons.dictionaryutils.DictionaryUtils import DictionaryUtils

from AICommons.aicommons.machinelearningmodels.AbstractMachineLearningModel import AbstractMachineLearningModel
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.utils.Constants import Constants

from CommonExceps.commonexceps.InitializationException import InitializationException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml import Pipeline


class NaiveBayesMachineLearningModelImpl(AbstractMachineLearningModel):

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def initialize_model(self, params_dict, label_column):
        """
        Instantiates a naive bayes model object

        :param label_column:
        :param params_dict:

        :return Naive Bayes instance
        """
        try:

            self.logger.info("Instantiating model object for naive bayes")
            self.logger.debug(
                "Parameters passed are: " + "labelCol=" + str(label_column) + "featuresCol=" +
                str(params_dict[CommonConstants.FEATURES_COLUMN_TAG]) +
                "smoothing=" + str(params_dict[CommonConstants.SMOOTHING_TAG]) +
                "learnPriors=" + str(params_dict[CommonConstants.LEARN_PRIORS_TAG]) +
                "preLearnedPriors=" + str(params_dict[CommonConstants.PRE_LEARNED_PRIORS_TAG])
            )


            model = MultinomialNB(alpha= params_dict[CommonConstants.SMOOTHING_TAG],
                                  class_prior= params_dict[CommonConstants.LEARN_PRIORS_TAG],
                                  fit_prior= params_dict[CommonConstants.PRE_LEARNED_PRIORS])




            self.logger.warning("Parameters passed to model object: " + str(model.get_params()))
            self.logger.info("Instantiated model object for naive bayes")
            return model

        except Exception as exp:
            self.logger.error('Exception occured while initializing Naive Bayes Model with params :  ' + str(
                params_dict) + ' label_column : ' + str(label_column))
            raise InitializationException(exp)



    def build_param_grid(self, model, params_dict):
        param_grid = ParamGridBuilder() \
            .addGrid(model.smoothing, params_dict[CommonConstants.SMOOTHING_TAG]) \
            .addGrid(model.modelType, params_dict[CommonConstants.MODEL_TYPE_TAG]) \
            .addGrid(model.thresholds, params_dict[CommonConstants.THRESHOLDS_TAG]) \
            .addGrid(model.weightCol, params_dict[CommonConstants.WEIGHT_COL_TAG]) \
            .build()
        return param_grid

    def get_loadable_object(self):
        """

        :return: decision tree model object
        """

        self.logger.info("Returning random forest model load object")
        return NaiveBayesModel()

    def get_default_params(self):
        """
        :return: random forest default params dict from common constants
        """

        return CommonConstants.NAIVE_BAYES_DEFAULT_PARAMS_DICT

    def evaluate_model_params(self, df, model_hyper_params):
        """
        This method evaluates some model specific params
        :param df:
        :param model_params:
        :return:
        """
        self.logger.info("Going to add class_weight column to the df")
        df = self.evaluate_class_weight(df, model_hyper_params)

        return df
