# TODO: Add docstring
class CommonConstants:



    # Logging related constants
    LOG_LEVEL_INFO = "Info"
    LOG_LEVEL_WARN = "Warn"
    LOG_LEVEL_ERROR = "Error"
    LOG_LEVEL_DEBUG = "Debug"

    CONFIG_LOGGER_TAG = "logger"
    CONFIG_LOGGER_PATH_TAG = "path"
    CONFIG_LOGGER_LEVEL_TAG = "level"
    FORMAT = '[%(asctime)s] [%(levelname)s] [%(module)s:%(funcName)s-%(lineno)d] - %(message)s'

    # Evaluation Service related constants
    PREDICTION_AND_LABEL_DF_KEY = 'predLabelKey'
    EVALUATION_METRICS_LIST_KEY = 'evaluationMetricKey'
    EVALUATION_RESP_KEY = 'evaluationRespKey'
    PRECISION_METRIC_ID = 'Precision'
    RECALL_METRIC_ID = 'Recall'
    FMEASURE_METRIC_ID = 'Fmeasure'
    FRAUD_CLASS_LABEL = '1.0'
    NON_FRAUD_CLASS_LABEL = '0.0'

    # Database related constants
    DATABASE_POSTGRES = "postgres"
    DATABASE_INFORMIX = "informix"
    DATABASE_CASSANDRA = "cassandra"
    DATABASE_HDFS = "HDFS"

    READ_DATA_COLUMNS_TAG = 'columns'

    TRUE_POSITIVE_METRIC_ID = 'TruePositive'
    FALSE_POSITIVE_METRIC_ID = 'FalsePositive'
    TRUE_NEGATIVE_METRIC_ID = 'TrueNegative'
    FALSE_NEGATIVE_METRIC_ID = 'FalseNegative'
    ACCURACY = 'Accuracy'
    FEATURE_WEIGHTAGE_METRIC_ID = 'FeatureWeightage'

    # Model related constants
    HDFS_MACHINE_LEARNING_MODELS_PATH_TAG = 'machine_learning_models'
    HDFS_TRANSFORMATIONS_PATH_TAG = "transformations_models"
    NAIVE_BAYES_TAG = "naive_bayes"
    # LABEL_COLUMN = ''
    TARGET_COLUMN_TAG = 'targetCol'
    KEY_IDENTIFIER = ''
    MODEL_KEY = "model_code"
    MAX_CATEGORICAL_FEATURE_UNIQUE_VALUE_COUNT = None
    RAW_PRED_COL = 'raw_prediction'
    PROBABILITY_COL = 'probability'
    PREDICTION_COL = 'prediction'

    # Default parameter dictionary key tags for machine learning models

    # For model_params
    MODEL_NAME_TAG = 'model_name'
    ENABLE_CV_TAG = 'enable_cv'
    FEATURE_LIST_TAG = 'feature_list'
    CONTINUOUS_FEATURES_TAG = 'continuous_features'
    CATEGORICAL_FEATURES_TAG = 'categorical_features'
    FEATURES_COLUMN_TAG = 'features_column'

    PREDICTION_COLUMN_TAG = 'prediction_column'
    PROBABILITY_COLUMN_TAG = 'probability_column'
    RAW_PREDICTION_COLUMN_TAG = 'raw_prediction_column'

    # For model_hyper_params
    SMOOTHING_TAG = 'smoothing'
    LEARN_PRIORS_TAG = "fitPriors"
    PRE_LEARNED_PRIORS_TAG = "classPriors"


    # Stats constants
    STATS_KEY_IDENTIFIER = "trace_audit_no"
    STATS_COLUMN_NAME = "prof_param_id"
    STATS_COLUMN_VALUE = "prof_param_value"

    # For cross_validation_params
    NUM_FOLDS_TAG = 'numFolds'
    SCORING_TAG = "scoringType"
    NUM_CORES_TAG = "numCores"
    IID_TAG = "independentIdenticallyDistributed"

    # Default parameter dictionaries for machine learning models


    NAIVE_BAYES_DEFAULT_PARAMS_DICT = {
        SMOOTHING_TAG: 1.0,
        LEARN_PRIORS_TAG: True,
        PRE_LEARNED_PRIORS_TAG: [0.5,0.5]
    }



    # Mapping Metadata Related constants

    # Tag names used in config
    METADATA_TAG = 'metadata'
    DATABASE_METADATA_TAG = 'database_metadata'
    QUERY_TAG = 'query'
    SCHEMA_TAG = 'schema'
    CARD_INSTANCES_SCHEMA_TAG = 'card_instances'
    CARDS_SCHEMA_TAG = 'cards'
    META_DATA_DICTIONARY_KEY_TAG = 'dictionary_key'
    META_DATA_DICTIONARY_VALUE_TAG = 'dictionary_value'


    # MAPPING VARIABLE TYPES
    VARIABLE_TYPE_STRING = 'string'
    VARIABLE_TYPE_DOUBLE = 'double'
    VARIABLE_TYPE_DECIMAL = 'decimal'
    VARIABLE_TYPE_TIME = 'time'

    HANDLER_TAG = 'handlers'
    FRAUD_ENGINE_HANDLER_TAG = 'fraud_engine_handler'
    COMMONS_HANDLER_TAG = 'commons_handler'
    PREPROCESSING_HANDLER_TAG = 'preprocessing_handler'
    MODEL_TRAIN_HANDLER_TAG = 'model_train_handler'
    PREDICTION_HANDLER_TAG = 'prediction_handler'
    FEATURE_ENGINEERING_HANDLER_TAG = 'feature_engineering_handler'
    TRANSFORMATION_HANDLER_TAG = 'transformation_handler'
    EVALUATION_HANDLER_TAG = 'evaluation_handler'
    HSM_GATEWAY_HANDLER_TAG = 'hsm_gateway_handler'
    MI_POOL_HANDLER_TAG = 'mi_pool_handler'
    DATABASE_HANDLER_TAG = 'database_handler'
    FILENAME_TAG = 'filename'
    PREDICTION_LOG_FOLDER_TAG = 'prediction'
    TRAINING_LOG_FOLDER_TAG = 'training'

    REPLACE_TYPE_DIGIT = 'digit'
    REPLACE_TYPE_SPECIAL_CHARACTER = 'special'

    SUB_DIR_PIPELINE_TAG = "pipeline"
    SUB_DIR_MAPPING_TAG = "mappings"
    CONFIG_HDFS_BASEPATH_TAG = 'hdfsbasepath'
    CONFIG_LABEL_TAG = 'label'

    NEW_FEATURE_LIST_TAG = 'new_features_list'
    FEATURE_ENGINEERING_FLOW_STANDARD = 'standard_flow'
    


    # NLP SHIT
    MAX_SEQ_LENGTH = 'MAX_SEQUENCE_LENGTH'
    CLASS_LABEL = 'CLASS_LABEL'
    MODEL_OUTPUT_DIR = 'MODEL_OUTPUT_DIR'
    SAVE_SUMMARY_STEPS = 'SAVE_SUMMARY_STEPS'
    SAVE_CHECKPOINTS_STEPS = 'SAVE_CHECKPOINTS_STEPS'
    LEARNING_RATE = 'LEARNING_RATE'
    BERT_MODEL_HUB = 'BERT_MODEL_HUB'
    NUM_TRAIN_EPOCHS = 'NUM_TRAIN_EPOCHS'
    WARMUP_PROPORTION = 'WARMUP_PROPORTION'
    NUM_TRAIN_STEPS = 'NUM_TRAIN_STEPS'
    NUM_WARM_STEPS = 'NUM_WARM_STEPS'
    TEST_OR_TRAIN = 'TEST_OR_TRAIN'
    LABEL_COLUMN_TAG = 'LABEL_COLUMN_TAG'
    BATCH_SIZE = 'BATCH_SIZE'