from AIModelTrain.aimodeltrain.driver.AbstractTrainDriverFactory import AbstractTrainDriverFactory
from pandas import DataFrame
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants




abs_train_driver_factory = AbstractTrainDriverFactory()

train_driver_inst = abs_train_driver_factory.get_instance()

from sklearn.datasets import load_breast_cancer

breast_cancer_data_set = load_breast_cancer()

training_df = DataFrame.from_records(breast_cancer_data_set.data, columns=breast_cancer_data_set.feature_names)

target = breast_cancer_data_set.target

model_params = {
    "model_name": "naive_bayes",
    "enable_cv": "N",
    "feature_list": training_df.columns.to_list(),
    "targetCol":  breast_cancer_data_set.target_names
}

model_hyper_params = {
    "smoothing": [0.1,0.2,0.3,0.4,0.5],
    "fitPriors": [True, False],
    "classPriors": [None]
}


model_cross_validator_params = {
    "numFolds": 5,
    "scoringType": "accuracy",
    "numCores": -1,
    "independentIdenticallyDistributed": "warn"
}






train_driver_inst.train_model(data=training_df, target=target, model_params=model_params, model_hyper_params=model_hyper_params, model_cross_validator_params=model_cross_validator_params)

