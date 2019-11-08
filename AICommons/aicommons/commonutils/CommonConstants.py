# TODO: Add docstring
class CommonConstants:

    # Spark related constants
    SPARK_CONTEXT = None
    SPARK_SESSION = None
    SPARK_CONF = None


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
    DECISION_TREE_TAG = "decision_tree"
    RANDOM_FOREST_TAG = "random_forest"
    GRADIENT_BOOSTED_TREE_TAG = "gradient_boosted_tree"
    LOGISTIC_REGRESSION_TAG = "logistic_regression"
    NAIVE_BAYES_TAG = "naive_bayes"
    MULTI_LAYER_PERCEPTRON_TAG = 'multi_layer_perceptron'
    LABEL_COLUMN = ''
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
    MAX_DEPTH_TAG = 'max_depth'
    MAX_BINS_TAG = 'max_bins'
    MIN_INSTANCES_PER_NODE_TAG = 'min_instances_per_node'
    MIN_INFO_GAIN_TAG = 'min_info_gain'
    MAX_MEMORY_IN_MB_TAG = 'max_memory_in_mb'
    CACHE_NODE_IDS_TAG = 'cache_node_ids'
    CHECKPOINT_INTERVAL_TAG = 'checkpoint_interval'
    IMPURITY_TAG = 'impurity'
    SEED_TAG = 'seed'
    NUM_TREES_TAG = 'num_trees'
    FEATURE_SUBSET_STRATEGY_TAG = 'feature_subset_strategy'
    SUB_SAMPLING_RATE_TAG = 'sub_sampling_rate'
    LOSS_TYPE_TAG = 'loss_type'
    MAX_ITER_TAG = 'max_iter'
    STEP_SIZE_TAG = 'step_size'
    FAMILY_TAG = 'family'
    STANDARDIZATION_TAG = 'standardization'
    ELASTIC_NET_PARAM_TAG = 'elasticNetParam'
    FIT_INTERCEPT_TAG = 'fitIntercept'
    THRESHOLD_TAG = 'threshold'
    THRESHOLDS_TAG = 'thresholds'
    TOL_TAG = 'tol'
    WEIGHT_COL_TAG = 'weightCol'
    WEIGHT_COL_NAME = 'column_name'
    BALANCING_RATIO_TAG = 'balancingRatio'
    REG_PARAM_TAG = 'regParam'
    AGGREGATION_DEPTH_TAG = 'aggregationDepth'
    SMOOTHING_TAG = 'smoothing'
    MODEL_TYPE_TAG = 'modelType'
    POSITIVE_LABEL_TAG = '1'
    NEGATIVE_LABEL_TAG = '0'
    LAYERS_TAG = 'layers'
    BLOCK_SIZE_TAG = 'block_size'
    SOLVER_TAG = 'solver'
    INITIAL_WEIGHTS_TAG = 'initial_weights'

    # Stats constants
    STATS_KEY_IDENTIFIER = "trace_audit_no"
    STATS_COLUMN_NAME = "prof_param_id"
    STATS_COLUMN_VALUE = "prof_param_value"

    # For cross_validation_params
    NUM_FOLDS_TAG = 'numFolds'

    # Default parameter dictionaries for machine learning models

    DECISION_TREE_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        PROBABILITY_COLUMN_TAG: PROBABILITY_COL,
        RAW_PREDICTION_COLUMN_TAG: RAW_PRED_COL,
        MAX_DEPTH_TAG: 5,
        MAX_BINS_TAG: 32,
        MIN_INSTANCES_PER_NODE_TAG: 1,
        MIN_INFO_GAIN_TAG: 0.0,
        MAX_MEMORY_IN_MB_TAG: 256,
        CACHE_NODE_IDS_TAG: False,
        CHECKPOINT_INTERVAL_TAG: 10,
        IMPURITY_TAG: 'gini',
        SEED_TAG: 0,
        NUM_FOLDS_TAG: 2
    }

    RANDOM_FOREST_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        PROBABILITY_COLUMN_TAG: PROBABILITY_COL,
        RAW_PREDICTION_COLUMN_TAG: RAW_PRED_COL,
        MAX_DEPTH_TAG: 5,
        MAX_BINS_TAG: 32,
        MIN_INSTANCES_PER_NODE_TAG: 1,
        MIN_INFO_GAIN_TAG: 0.0,
        MAX_MEMORY_IN_MB_TAG: 256,
        CACHE_NODE_IDS_TAG: False,
        CHECKPOINT_INTERVAL_TAG: 10,
        IMPURITY_TAG: 'gini',
        NUM_TREES_TAG: 20,
        FEATURE_SUBSET_STRATEGY_TAG: "auto",
        SEED_TAG: 0,
        SUB_SAMPLING_RATE_TAG: 1.0,
        NUM_FOLDS_TAG: 2
    }

    GRADIENT_BOOSTED_TREE_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        MAX_DEPTH_TAG: 5,
        MAX_BINS_TAG: 32,
        MIN_INSTANCES_PER_NODE_TAG: 1,
        MIN_INFO_GAIN_TAG: 0.0,
        MAX_MEMORY_IN_MB_TAG: 256,
        CACHE_NODE_IDS_TAG: False,
        CHECKPOINT_INTERVAL_TAG: 10,
        LOSS_TYPE_TAG: 'logistic',
        MAX_ITER_TAG: 20,
        STEP_SIZE_TAG: 0.1,
        SEED_TAG: 0,
        SUB_SAMPLING_RATE_TAG: 1.0
    }

    LOGISTIC_REGRESSION_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        PROBABILITY_COLUMN_TAG: PROBABILITY_COL,
        RAW_PREDICTION_COLUMN_TAG: RAW_PRED_COL,
        FAMILY_TAG: 'binomial',
        MAX_ITER_TAG: 100,
        STANDARDIZATION_TAG: True,
        ELASTIC_NET_PARAM_TAG: 0.0,
        FIT_INTERCEPT_TAG: True,
        THRESHOLD_TAG: 0.5,
        THRESHOLDS_TAG: [0.5,0.5],
        TOL_TAG: 0.000001,
        WEIGHT_COL_TAG: LABEL_COLUMN,
        REG_PARAM_TAG: 0.0,
        AGGREGATION_DEPTH_TAG: 2,
        NUM_FOLDS_TAG: 2,
        BALANCING_RATIO_TAG: 0.9
    }

    NAIVE_BAYES_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        PROBABILITY_COLUMN_TAG: PROBABILITY_COL,
        RAW_PREDICTION_COLUMN_TAG: RAW_PRED_COL,
        SMOOTHING_TAG: 1.0,
        MODEL_TYPE_TAG: 'multinomial',
        THRESHOLDS_TAG: [0.5, 0.5],
        WEIGHT_COL_TAG: LABEL_COLUMN
    }

    MULTI_LAYER_PERCEPTRON_DEFAULT_PARAMS_DICT = {
        PREDICTION_COLUMN_TAG: PREDICTION_COL,
        PROBABILITY_COLUMN_TAG: PROBABILITY_COL,
        RAW_PREDICTION_COLUMN_TAG: RAW_PRED_COL,
        MAX_ITER_TAG: 1.0,
        SEED_TAG: 0,
        LAYERS_TAG: [16,10,10,2],
        BLOCK_SIZE_TAG: 128,
        STEP_SIZE_TAG: 0.03,
        TOL_TAG: 0.000001,
        SOLVER_TAG: 'l-bfgs'
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
    
    #  Anomaly detection related constants
    ANOMALY_DETECTION_TECHNIQUE_NAME = 'anomaly_detection_technique_name'
    HBOS_TAG = 'HBOS'
    HBOS_CATEGORICAL_TAG = 'HBOS_CATEGORICAL'
    HBOS_CONTINUOUS_TAG = 'HBOS_CONTINUOUS'
    CARD_NO_TAG = 'card_srno'
    COUNT_TAG = 'count'
    NORM_COUNT_TAG = 'count_norm'
    MIN_COUNT_TAG = 'min_count'
    MAX_COUNT_TAG = 'max_count'
    HDFS_WEB_PORT = '50070'
    HDFS_PORT = '9000'
    MIN_TAG = 'min'
    MAX_TAG = 'max'
    NUMBER_OF_BINS = 'number_of_bins'
    ANOMALY_SCORE_COLUMN_TAG = 'anomaly_score_column'
    IS_FRAUD_COLUMN_TAG = 'is_fraud'
    TRACE_AUDIT_NO_TAG = 'trace_audit_no'
    MODEL_BASED_FEATURES_HISTOGRAMS_DICT = None
    ANOMALY_THRESHOLD_TAG = 'anomaly_threshold'
    USER_TAG = 'user'
    PASSWORD_TAG = 'password'
    DRIVER_TAG = 'driver'
    LABEL_COLUMN_TAG = 'label'
    BATCH_SIZE = 10000

