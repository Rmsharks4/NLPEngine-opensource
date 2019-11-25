"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an implementation of abstract machine learning model class, it is meant to create and handle model
specific operations for Naive-Bayes.

Class Functions:
_init_


"""

import logging

from sklearn.naive_bayes import MultinomialNB


from AICommons.aicommons.machinelearningmodels.AbstractMachineLearningModel import AbstractMachineLearningModel
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.utils.Constants import Constants
from CommonExceps.commonexceps.InitializationException import InitializationException


class NaiveBayesMachineLearningModelImpl(AbstractMachineLearningModel):

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def initialize_model(self, params_dict):
        """
        Instantiates a naive bayes model object

        :param params_dict:
        :return Naive Bayes instance
        """
        try:

            self.logger.info("Instantiating model object for naive bayes")
            self.logger.debug(
                "Parameters passed are: " +
                "feature_list= " + str(params_dict[CommonConstants.FEATURE_LIST_TAG]) +
                "smoothing= " + str(params_dict[CommonConstants.SMOOTHING_TAG]) +
                "learnPriors= " + str(params_dict[CommonConstants.LEARN_PRIORS_TAG]) +
                "preLearnedPriors= " + str(params_dict[CommonConstants.PRE_LEARNED_PRIORS_TAG])
            )

            model = MultinomialNB()

            smoothing = params_dict[CommonConstants.SMOOTHING_TAG]
            pre_learned_priors = params_dict[CommonConstants.PRE_LEARNED_PRIORS_TAG]
            learn_priors_from_data = params_dict[CommonConstants.LEARN_PRIORS_TAG]

            all_params_are_lists = isinstance(smoothing, list) and isinstance(pre_learned_priors, list) and\
                                   isinstance(learn_priors_from_data, list)

            if not all_params_are_lists:
                model.set_params(alpha=smoothing, class_prior=pre_learned_priors, fit_prior=learn_priors_from_data)
                self.logger.warning("Parameters passed to model object: " + str(model.get_params()))
            else:
                self.logger.warning("Model set to default parameters: " + str(model.get_params()))

            self.logger.info("Instantiated model object for naive bayes")
            return model

        except Exception as exp:
            self.logger.error('Exception occured while initializing Naive Bayes Model with params: ' +
                              str(params_dict))
            raise InitializationException(exp)

    def build_param_grid(self, params_dict):
        parameter_grid = {
            "alpha": params_dict[CommonConstants.SMOOTHING_TAG],
            "class_prior": params_dict[CommonConstants.PRE_LEARNED_PRIORS_TAG],
            "fit_prior": params_dict[CommonConstants.LEARN_PRIORS_TAG]
        }
        return parameter_grid

    def get_model_params(self, model):
        return model.get_params()

    def get_loadable_object(self):
        """

        :return: Naive-Bayes model instance
        """

        self.logger.info("Returning Naive-Bayes loaded model instance")
        return MultinomialNB()

    def get_default_params(self):
        """
        :return: Naive-Bayes default params dict from common constants
        """

        return CommonConstants.NAIVE_BAYES_DEFAULT_PARAMS_DICT
