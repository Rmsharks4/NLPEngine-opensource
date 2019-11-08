
import logging

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import VectorIndexer
from pyspark.sql.functions import udf
import pyspark.sql.functions as Functions

from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.utils.Constants import Constants
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException

from pyspark.sql.types import TimestampType, DateType, IntegerType, FloatType, DoubleType, StringType, BooleanType
from pyspark.sql.functions import countDistinct,col, array_max


class DataFrameUtils:
    """
    Implement the operations to create concrete product objects.
    """

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def drop_column(cls, df, column_names):
        """
        :param df: Dataframe
        :param column_names: list of columns that need to be removed
        :return: Dataframe with remaining columns
        """

        try:
            df = df.select([c for c in df.columns if c not in column_names])
        except Exception as exp:
            cls.logger.error('Exception occured while dropping columns : ' + str(column_names) + ' from dataframe : ' + str(df))
            raise DataFrameException(exp)
        return df

    @classmethod
    def get_max_unique_count(cls, df, feature_list):
        """
         author: hrafiq@i2cinc.com
         Get the maximum unique value count of a categorical features

        :param pipeline_model: pipeline_model containing categorical features unique values lists
        :return:
        """
        try:
            cls.logger.info("Getting maximum unique value count from given dataframe and feature list " + str(feature_list))
            unique_count_row = df.agg(*(countDistinct(col(c)).alias(c) for c in feature_list)).head()
            cls.logger.warning("Count distinct categories: " + str(unique_count_row))
            max_count = max(unique_count_row)
            cls.logger.warning("Maximum unique count: " + str(max_count))
            return max_count

        except Exception as exp:
            cls.logger.error("Exception occured while getting max unique value count ")
            raise CommonBaseException(exp)
    @classmethod
    def stratified_train_test_split(cls, df, test_ratio=0.30):
        """
        author: afarooq01@i2cinc.com
        Splits the data into a stratified train and test set according to given ratio

        :param df: dataframe containing data to be split
        :param test_ratio: ratio of data to be used for testing
        :return: train and test data sets
        """
        try:
            cls.logger.info("Stratifying column: " + str(CommonConstants.LABEL_COLUMN))
            cls.logger.info("Test ratio: " + str(test_ratio))
            cls.logger.info("Splitting data")
            test_set = df.stat.sampleBy(CommonConstants.LABEL_COLUMN, fractions={True: test_ratio,False: test_ratio})
            cls.logger.info('Data frame columns : ' +str(df.columns))
            # cloned_df = CommonConstants.SPARK_SESSION.createDataFrame(df.rdd, df.schema)
            train_set = df.join(test_set, [CommonConstants.KEY_IDENTIFIER], "leftanti")
            cls.logger.info("Data split into train test sets")
            cls.logger.info("Train data count: " + str(train_set.count()))
            cls.logger.info("Test data count: " + str(test_set.count()))
            return train_set, test_set

        except Exception as exp:
            cls.logger.error(
                'Exception occured while splitting train and test dataset')
            raise DataFrameException(exp)

        #TODO: shift vectorizing functions from DataFame Utils to a suitable folder
    @classmethod
    def vectorize_data(cls, feature_list, max_categories, features_column="features"):
        vec_assembler = None
        vec_indexer = None
        cls.logger.info("Going to vector assemble data")
        vec_assembled_features_column = "assembled_features"
        vec_assembler = DataFrameUtils.vector_assemble(feature_list=feature_list,output_column=vec_assembled_features_column)
        cls.logger.warning(
            "Vector assembled column: " + str(vec_assembled_features_column) +
            " with features: " + str(feature_list))
        cls.logger.info("Data successfully vector assembled")

        if max_categories > 0:

            cls.logger.info("Going to vector index data")
            cls.logger.warning(
                "Columns to vector index: " + str(vec_assembled_features_column))
            vec_indexer = DataFrameUtils.vector_index(input_column=vec_assembled_features_column,
                                                           max_categories=max_categories,
                                                           output_column=features_column)
            cls.logger.warning(
                "Vector indexed column: " + features_column +
                " with features: " + str(vec_assembled_features_column))
            cls.logger.info("Data successfully vector indexed")


        return vec_assembler, vec_indexer

    @classmethod
    def vector_assemble(cls, feature_list, output_column="assembled_features"):
        """
        author: afarooq01@i2cinc.com
        Appends a column to the df, containing all the values of required columns for every record.

        :param df: dataframe containing data to be processed
        :param feature_list: list of required columns to be considered for vector assembling
        :param features_column: name for the newly appended column
        :return: vector assembled df
        """
        try:
            cls.logger.debug("Columns to vector assemble: " + str(feature_list))
            cls.logger.info("Vector assembling data")
            vector_assembler = VectorAssembler(inputCols=feature_list, outputCol=output_column)
            return vector_assembler

        except Exception as exp:
            cls.logger.error(
                'Exception occured while applying vector assembler using feature_list : ' +str(feature_list))
            raise DataFrameException(exp)


    @classmethod
    def vector_index(cls, input_column, max_categories, output_column="features"):
        """
        author: afarooq01@i2cinc.com
        Appends a column to the df, containing all the values of required columns for every record.

        :param df: dataframe containing data to be processed
        :param feature_list: list of required columns to be considered for vector assembling
        :param features_column: name for the newly appended column
        :return: vector assembled df
        """
        try:
            cls.logger.debug("Columns to vector index: " + str(input_column))
            cls.logger.info("Vector indexing data")
            vector_indexer = VectorIndexer(inputCol=input_column, outputCol=output_column, maxCategories=max_categories,
                                            handleInvalid='keep')
            return vector_indexer

        except Exception as exp:
            cls.logger.error(
                'Exception occured while applying vector indexer using feature_list : ' + str(input_column))
            raise DataFrameException(exp)

    @classmethod
    def add_column_with_one_value(cls, df, column_name, column_value):
        """
        author: afarooq01@i2cinc.com
        Appends a column to df with one value

        :param df: dataframe
        :param column_name: name of newly appended column
        :param column_value: column value to fill the column with
        :return: df with appended column
        """
        try:

            cls.logger.info("Adding single value: " + str(column_value) + " throughout the column of: " + str(column_name))
            col_val = udf(lambda x: str(column_value))
            updated_df = df.withColumn(column_name, col_val(df[CommonConstants.KEY_IDENTIFIER]))
            cls.logger.info("Column with one value added: " + str(updated_df.columns))
            return updated_df

        except Exception as exp:
            cls.logger.error(
                'Exception occured while adding column : ' + str(column_name) +' with one value : ' + str(column_value))
            raise DataFrameException(exp)


    @classmethod
    def convert_column_type(cls, df, column_to_convert, required_col_type, new_col_name):
        """
        author: sfatima@i2cinc.com
        Converts the column type of a df column

        :param column_to_convert: string type
        :param required_col_type: string type
        :param new_col_name: string type
        :return: df with converted column type
        """
        try:
            df = df.withColumn(new_col_name, df[column_to_convert].cast(required_col_type))
            return df

        except Exception as exp:
            cls.logger.error(
                'Exception occured while converting column ' +str(column_to_convert) + ' to type '+str(required_col_type))
            raise DataFrameException(exp)

    @classmethod
    def check_df_for_string_type_column(cls, df):
        """
        author: sfatima@i2cinc.com
        Checks if Dataframe has string type column

        :param df: (pyspark dataframe)
        :return: ---
        """
        try:
            types = [f.dataType for f in df.schema.fields]
            for element in types:
                if element == "StringType":
                    raise DataFrameException('Dataframe contains String Type column!')

        except Exception as exp:
            cls.logger.error(
                'Exception occured while checking string types in df : '+str(df))
            raise DataFrameException(exp)

    @classmethod
    def split_column(cls, df, column_name, splitting_character, selector_index):
        """
        author: hrafiq@i2cinc.com
        Splits the column with given splitting character

        :param df: (pyspark dataframe)
        :param column_name: column to split
        :param splitting_character:
        :return: df : df with splitted column
        """
        try:
            split_col = Functions.split(df[column_name], splitting_character)
            df = df.withColumn(column_name, (split_col.getItem(selector_index)))
            return df
        except Exception as exp:
            cls.logger.error(
                'Exception occured while splitting column' + str(column_name) + '  from dataframe ' + str(df))
            raise DataFrameException(exp)

    @classmethod
    def select_columns_from_dataframe(cls, df, columns_list):
        """
        authors: smahmood@i2cinc.com
        Selects given columns from dataframe

        :param df: pyspark dataframe
        :param columns_list: list of column names to be included in new dataframe
        :return: dataframe containing given column list only
        """
        try:
            df = df.select([c for c in df.columns if c in columns_list])
            return df

        except Exception as exp:
            cls.logger.error(
                'Exception occured while selecting columns from dataframe : ' + str(df))
            raise DataFrameException(exp)


    @classmethod
    def check_columns_existence_in_dataframe(cls, dataframe_columns, columns_list):
        """
        authors: smahmood@i2cinc.com
        Checks if given list of columns exists in dataframe columns list

        :param dataframe_columns: list of columns of a dataframe
        :param columns_list: list of column names
        :return: True if columns list exists, False otherwise
        """
        if (set(columns_list).issubset(set(dataframe_columns))):
            return True
        else:
            return False


    @classmethod
    def join_dataframes(cls, df1, df2, join_key):
        try:
            joined_df = df1.join(df2, [join_key])
            return joined_df

        except Exception as exp:
            cls.logger.error(
                'Exception occured while joining dataframes df1: ' + str(df1) + ' and df2: ' +str(df2))
            raise DataFrameException(exp)

    @classmethod
    def join_dataframe_without_key(cls, df1, df2):
        try:

            df1 = DataFrameUtils.add_column_with_one_value(df1, "id", 0)
            df2 = DataFrameUtils.add_column_with_one_value(df2, "id", 0).drop(CommonConstants.KEY_IDENTIFIER)

            joined_df = df1.join(df2, "id").drop("id")
            return joined_df

        except Exception as exp:
            cls.logger.error(
                'Exception occured while joining dataframes df1: ' + str(df1) + ' and df2: ' +str(df2))
            raise DataFrameException(exp)

    @classmethod
    def rename_column(cls, df, existing_col_name, new_col_name):
        try:
            new_df = df.withColumnRenamed(existing_col_name, new_col_name)
            #new_cloned_df = CommonConstants.SPARK_SESSION.createDataFrame(new_df.rdd, new_df.schema)
            return new_df
        except Exception as exp:
            cls.logger.error(
                'Exception occured while renaming column ' + str(existing_col_name)+ ' to ' + str(new_col_name))
            raise DataFrameException(exp)

    @staticmethod
    def get_data_type(data_type_value):
        if data_type_value == 'date_type':
            return DateType()
        if data_type_value == 'timestamp_type':
            return TimestampType()
        if data_type_value == 'integer_type':
            return IntegerType()
        if data_type_value == 'float_type':
            return FloatType()
        if data_type_value == 'double_type':
            return DoubleType()
        if data_type_value == 'string_type':
            return StringType()
        if data_type_value == 'boolean_type':
            return BooleanType()

    @classmethod
    def filter_dataframe_by_column_list(cls, df, read_data_dict, model_id, version_id, train_test_prediction_mode):
        try:
            cls.logger.warning("Going to filter dataframe for given column list for model_id: " + str(model_id) +
                                " version_id: " + str(version_id))

            if read_data_dict is None:
                cls.logger.error("MissingMandatoryFieldException : read data configs are not defined for model_id: " +
                                  str(model_id) + " version_id: " + str(version_id))
                raise MissingMandatoryFieldException("read data configs are not defined for model_id: " +
                                                     str(model_id) + " version_id: " + str(version_id))

            model_specific_data_columns = list(read_data_dict.get(CommonConstants.READ_DATA_COLUMNS_TAG, None))

            if model_specific_data_columns is None:
                cls.logger.error("MissingMandatoryFieldException : Read Data columns are not defined for model_id: " +
                                  str(model_id) + " version_id: " + str(version_id))
                raise MissingMandatoryFieldException("Read Data columns are not defined for model_id: " +
                                                     str(model_id) + " version_id: " + str(version_id))

            if train_test_prediction_mode in ['0','1','2']:
                model_specific_data_columns.append(CommonConstants.KEY_IDENTIFIER)
                model_specific_data_columns.append(CommonConstants.LABEL_COLUMN)
            else:
                model_specific_data_columns.append(CommonConstants.KEY_IDENTIFIER)

            cls.logger.warning("filtering dataframe for given column list: " + str(model_specific_data_columns))
            model_specific_input_df = df.select(model_specific_data_columns)

            return model_specific_input_df
        except MissingMandatoryFieldException as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            cls.logger.error('Exception occured while fetching model specific configurations')
            raise CommonBaseException(exp)