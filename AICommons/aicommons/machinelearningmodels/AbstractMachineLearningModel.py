"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an Abstract Machine Learning Model class, with functions generically applicable to all models (
or overridden).

Class Functions:
initialize_model
train
predict
get_model_params
get_default_params
build_param_grid
perform_cross_validation

"""

import logging

from abc import ABC, abstractmethod
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AICommons.aicommons.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from sklearn.model_selection import GridSearchCV


class AbstractMachineLearningModel(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @abstractmethod
    def initialize_model(self, params_dict):
        pass

    @classmethod
    def train(cls, model, data, target, params_dict):
        """
        Trains model on the provided data

        :param model: model object to be trained
        :param data: dataframe of the training data features
        :param target: outcome associated with the training data features
        :return: trained model object
        """
        try:
            cls.logger.info("Fitting model")
            cls.logger.debug("Data frame columns: " + str(data.columns))
            trained_model = model.fit(data, target)
            cls.logger.info("Model fitted")
            return trained_model

        except Exception as exp:
            cls.logger.error('Exception occured while training data to model : ' + str(model))
            raise CommonBaseException(exp)


    @classmethod
    def predict(cls, model, data, params_dict):
        """
        Makes predictions on data using a trained model object

        :param model: model object to be used for predictions
        :param data: dataframe with data to make predictions on
        :return: An array of the target predictions
        """
        try:
            cls.logger.info("Predicting on data")
            cls.logger.debug("Dataframe columns: " + str(data.columns))
            predicted_data = model.predict(data)
            cls.logger.info("Predictions made")
            return predicted_data

        except Exception as exp:
            cls.logger.error('Exception occured while predicting data from model : ' + str(model))
            raise CommonBaseException(exp)

    @abstractmethod
    def get_loadable_object(self):
        pass

    @abstractmethod
    def get_model_params(self, model):
        pass

    @abstractmethod
    def get_default_params(self):
        pass

    @abstractmethod
    def build_param_grid(self, params_dict):
        pass

    @classmethod
    def perform_cross_validation(cls, model, data, target, params_dict):
        """
        performs cross validation to get the best learned model

        :param model: the estimator to be cross-validated
        :param data:  dataframe of the training data features
        :param target: outcome associated with the training data features
        :param params_dict: contains both the model hyper parameter grid as well as the grid search parameters


        :return: A model tuned over the parameter search space.
        """
        try:
            cls.logger.warning("Building a Parameter grid for tuning model on a set of hyper parameters ")
            param_grid = cls.build_param_grid(cls,params_dict)

            cls.logger.info("Instantiating Grid Search Cross Validator object")
            grid_search_clf = GridSearchCV(estimator=model,
                                           param_grid=param_grid,
                                           scoring=params_dict[CommonConstants.SCORING_TAG],
                                           cv=params_dict[CommonConstants.NUM_FOLDS_TAG],
                                           n_jobs=params_dict[CommonConstants.NUM_CORES_TAG],
                                           iid=params_dict[CommonConstants.IID_TAG])
            cls.logger.info("Instantiated  Grid Search Cross Validator object")

            cls.logger.warning("Fitting models using Cross Validator")
            cls.logger.warning("Data frame columns: " + str(data.columns.to_list() + params_dict[CommonConstants.TARGET_COLUMN_TAG].tolist()))

            cv_model = grid_search_clf.fit(data, target)
            cls.logger.warning("Model fitted")

            return cv_model

        except Exception as exp:
            cls.logger.error("Exception: Cross validation couldn't be performed")
            raise CommonBaseException(exp)


