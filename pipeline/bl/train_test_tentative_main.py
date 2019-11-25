from pipeline.bl.ModelDataTrainingAndTestingHandler import ModelDataTrainingAndTestingHandler
from pandas import DataFrame
from sklearn.model_selection import train_test_split

train_test_service_handler= ModelDataTrainingAndTestingHandler()

from sklearn.datasets import load_breast_cancer

breast_cancer_data_set = load_breast_cancer()

data = DataFrame.from_records(breast_cancer_data_set.data, columns=breast_cancer_data_set.feature_names)
target = breast_cancer_data_set.target

train_df, test_df, train_target, test_target = train_test_split(data,target, test_size=0.15, random_state=42)

model_parameters = {
    "model_name": "naive_bayes",
    "enable_cv": "N",
    "feature_list": data.columns.to_list(),
    "targetCol":  breast_cancer_data_set.target_names
}

model_hyper_parameters = {
    "smoothing": 0.4,
    "fitPriors": True,
}


model_cross_validator_params = {
    "numFolds": 5,
    "scoringType": "accuracy",
    "numCores": -1,
    "independentIdenticallyDistributed": "warn"
}


trained_model= train_test_service_handler.perform_model_training(train_df, train_target, model_parameters, model_hyper_parameters, model_cross_validator_params)

train_test_service_handler.perform_model_testing(test_df, model_parameters, trained_model)
