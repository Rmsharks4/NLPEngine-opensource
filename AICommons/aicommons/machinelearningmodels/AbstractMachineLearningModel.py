"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an Abstract Machine Learning Model class, with functions generically applicable to all models (
or overridden).

Class Functions:
initialize_model
train
predict
get_debug_string
get_load_object

"""

import logging

from abc import ABC, abstractmethod

from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AICommons.aicommons.utils.Constants import Constants
from AICommons.aicommons.dictionaryutils.DictionaryUtils import DictionaryUtils
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from sklearn.model_selection import GridSearchCV


class AbstractMachineLearningModel(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @abstractmethod
    def initialize_model(self, params_dict, label_column):
        pass

    @classmethod
    def train(cls, model, data):
        """
        Trains model on the provided data

        :param model: model object to be trained
        :param data: dataframe with training data for model
        :return: trained model object
        """
        try:
            cls.logger.info("Fitting model")
            cls.logger.debug("Data frame columns: " + str(data.columns))
            trained_model = model.fit(data)
            cls.logger.info("Model fitted")
            return trained_model

        except Exception as exp:
            cls.logger.error('Exception occured while training data to model : ' + str(model))
            raise CommonBaseException(exp)

    @classmethod
    def predict(cls, model, data):
        """
        Makes predictions on data using a trained model object

        :param model: model object to be used for predictions
        :param data: dataframe with data to make predictions on
        :return: initial datafarme with predictions appended to it
        """
        try:
            cls.logger.info("Predicting on data")
            cls.logger.debug("Dataframe columns: " + str(data.columns))
            predicted_data = model.predict(data)
            cls.logger.info("Predictions made")
            cls.logger.debug("Predicted data columns: " + str(predicted_data.columns))
            return predicted_data

        except Exception as exp:
            cls.logger.error('Exception occured while predicting data from model : ' + str(model))
            raise CommonBaseException(exp)

    @abstractmethod
    def get_loadable_object(self):
        pass

    @abstractmethod
    def get_default_params(self):
        pass

    @abstractmethod
    def evaluate_model_params(self, df, model_params):
        pass

    @classmethod
    def evaluate_class_weight(self, df, model_hyper_params):
        """
                :param df: dataframe
                :param parameter_dict: parameters dictionary
                :return: pyspark dataframe with new feature feature added
                """
        try:
            self.logger.warning("Loading parameters from model_hyper_param dictionary")

            is_fraud = CommonConstants.LABEL_COLUMN
            balancing_ratio = model_hyper_params[CommonConstants.WEIGHT_COL_TAG][CommonConstants.BALANCING_RATIO_TAG]
            class_weight_col = model_hyper_params[CommonConstants.WEIGHT_COL_TAG][CommonConstants.WEIGHT_COL_NAME]

            self.logger.warning("Adding new column(feature): " + class_weight_col + ", to the dataframe")
            df = df.withColumn(class_weight_col, when(df[is_fraud] == True,
                                                      balancing_ratio[CommonConstants.POSITIVE_LABEL_TAG]).otherwise(
                balancing_ratio[CommonConstants.NEGATIVE_LABEL_TAG]))
            self.logger.warning(class_weight_col + ", added to dataframe succesfully")
            # df.show()
            return df
        except (MissingMandatoryFieldException, InvalidInfoException) as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            raise DataFrameException(exp)

    def perform_cross_validation(self, train_df, params_dict, model):
        """
        performs cross validation to get the best learned model

        :param train_df: dataframe to be fitted on model
        :param label_column: labeled column in dataframe
        :param params_dict: contains model_paramters
        :param model:

        :return best decision tree model
        """
        try:

            self.logger.warning("Building a Parameter grid for tuning model on a set of hyper parameters ")
            param_grid = self.build_param_grid(model, params_dict)

            self.logger.info("Instantiating Grid Search Cross Validator object")
            grid_search_clf = GridSearchCV(estimator=model,
                                           param_grid=param_grid,
                                           scoring=params_dict[CommonConstants.SCORING_TAG],
                                           cv=params_dict[CommonConstants.NUM_FOLDS_TAG],
                                           n_jobs=params_dict[CommonConstants.NUM_CORES_TAG],
                                           iid=params_dict[CommonConstants.IID_TAG])
            self.logger.info("Instantiated  Grid Search Cross Validator object")

            self.logger.warning("Fitting models using Cross Validator")
            self.logger.warning("Data frame columns: " + str(train_df.columns))
            train_df.show()

            # todo Have to slice the dataframe in the features' list set
            cv_model = grid_search_clf.fit(train_df[CommonConstants.FEATURE_LIST_TAG],
                                           train_df[CommonConstants.TARGET_TAG])
            self.logger.warning("Model fitted")

            return cv_model

        except Exception as exp:
            self.logger.error("Exception: Cross validation couldn't be performed")
            raise CommonBaseException(exp)


