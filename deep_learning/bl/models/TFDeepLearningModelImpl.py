from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from AICommons.aicommons.machinelearningmodels.AbstractMachineLearningModel import AbstractMachineLearningModel
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import pickle
import bert
from bert import run_classifier
from bert import optimization
from bert import tokenization
import warnings
from sklearn.model_selection import train_test_split
import functools


class TFDeepLearningModelImpl(AbstractMachineLearningModel, StandardConfigParserImpl):

    params = None

    def __init__(self):
        super().__init__()

    def initialize_model(self, params_dict):
        """
        :param params_dict:
        CommonConstants.MODEL_OUTPUT_DIR:
        CommonConstants.SAVE_SUMMARY_STEPS:
        CommonConstants.SAVE_CHECKPOINTS_STEPS:
        CommonConstants.BERT_MODEL_HUB:
        CommonConstants.CLASS_LABEL:
        CommonConstants.LEARNING_RATE:
        CommonConstants.NUM_TRAIN_STEPS:
        CommonConstants.NUM_WARM_STEPS:
        CommonConstants.TEST_OR_TRAIN:
        CommonConstants.BATCH_SIZE:
        CommonConstants.READ_DATA_COLUMNS_TAG:
        CommonConstants.LABEL_COLUMN_TAG:
        CommonConstants.MAX_SEQ_LENGTH:
        CommonConstants.NUM_TRAIN_EPOCHS
        CommonConstants.WARMUP_PROPORTION
        :return:
        """

        self.params = params_dict

        run_config = tf.compat.v1.estimator.RunConfig(
            model_dir=self.params[CommonConstants.MODEL_OUTPUT_DIR],
            save_summary_steps=self.params[CommonConstants.SAVE_SUMMARY_STEPS],
            save_checkpoints_steps=self.params[CommonConstants.SAVE_CHECKPOINTS_STEPS])

        model_fn = self.model_fn_builder(
            bert_model_hub=self.params[CommonConstants.BERT_MODEL_HUB],
            num_labels=len(self.params[CommonConstants.CLASS_LABEL]),
            learning_rate=self.params[CommonConstants.LEARNING_RATE],
            num_train_steps=self.params[CommonConstants.NUM_TRAIN_STEPS],
            num_warmup_steps=self.params[CommonConstants.NUM_WARM_STEPS],
            is_predicting=self.params[CommonConstants.TEST_OR_TRAIN])

        estimator = tf.estimator.Estimator(
            model_fn=model_fn,
            config=run_config,
            params={"batch_size": self.params[CommonConstants.BATCH_SIZE]})

        return estimator

    @classmethod
    def model_fn_builder(cls, bert_model_hub, num_labels, learning_rate, num_train_steps,
                         num_warmup_steps, is_predicting):

        def model_fn(features, labels, mode, params):

            input_ids = features["input_ids"]
            input_mask = features["input_mask"]
            segment_ids = features["segment_ids"]
            label_ids = features["label_ids"]

            if not is_predicting:

                (loss, predicted_labels, log_probs) = cls.create_model(
                    bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, label_ids, num_labels)

                train_op = bert.optimization.create_optimizer(
                    loss, learning_rate, num_train_steps, num_warmup_steps, use_tpu=False)

                eval_metrics = cls.metric_fn(label_ids, predicted_labels)

                if mode == tf.compat.v1.estimator.ModeKeys.TRAIN:
                    return tf.compat.v1.estimator.EstimatorSpec(mode=mode,
                                                                loss=loss,
                                                                train_op=train_op)
                else:
                    return tf.compat.v1.estimator.EstimatorSpec(mode=mode,
                                                                loss=loss,
                                                                eval_metric_ops=eval_metrics)

            else:
                (predicted_labels, log_probs) = cls.create_model(
                    bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, label_ids, num_labels)
                predictions = {
                    'probabilities': log_probs,
                    'labels': predicted_labels
                }
                return tf.compat.v1.estimator.EstimatorSpec(mode, predictions=predictions)

        return model_fn

    @classmethod
    def metric_fn(cls, label_ids, predicted_labels):
        accuracy = tf.compat.v1.metrics.accuracy(label_ids, predicted_labels)
        f1_score = tf.contrib.metrics.f1_score(
            label_ids,
            predicted_labels)
        auc = tf.compat.v1.metrics.auc(
            label_ids,
            predicted_labels)
        recall = tf.compat.v1.metrics.recall(
            label_ids,
            predicted_labels)
        precision = tf.compat.v1.metrics.precision(
            label_ids,
            predicted_labels)
        true_pos = tf.compat.v1.metrics.true_positives(
            label_ids,
            predicted_labels)
        true_neg = tf.compat.v1.metrics.true_negatives(
            label_ids,
            predicted_labels)
        false_pos = tf.compat.v1.metrics.false_positives(
            label_ids,
            predicted_labels)
        false_neg = tf.compat.v1.metrics.false_negatives(
            label_ids,
            predicted_labels)
        return {
            "eval_accuracy": accuracy,
            "f1_score": f1_score,
            "auc": auc,
            "precision": precision,
            "recall": recall,
            "true_positives": true_pos,
            "true_negatives": true_neg,
            "false_positives": false_pos,
            "false_negatives": false_neg
        }

    @classmethod
    def create_model(cls, bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, labels,
                     num_labels):

        bert_module = hub.Module(
            bert_model_hub,
            trainable=True)
        bert_inputs = dict(
            input_ids=input_ids,
            input_mask=input_mask,
            segment_ids=segment_ids)
        bert_outputs = bert_module(
            inputs=bert_inputs,
            signature="tokens",
            as_dict=True)

        output_layer = bert_outputs["pooled_output"]

        hidden_size = output_layer.shape[-1].value

        output_weights = tf.compat.v1.get_variable(
            "output_weights", [num_labels, hidden_size],
            initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.02))

        output_bias = tf.compat.v1.get_variable(
            "output_bias", [num_labels], initializer=tf.compat.v1.zeros_initializer())

        with tf.compat.v1.variable_scope("loss"):
            output_layer = tf.compat.v1.nn.dropout(output_layer, keep_prob=0.9)

            logits = tf.compat.v1.matmul(output_layer, output_weights, transpose_b=True)
            logits = tf.compat.v1.nn.bias_add(logits, output_bias)
            log_probs = tf.compat.v1.nn.log_softmax(logits, axis=-1)

            one_hot_labels = tf.compat.v1.one_hot(labels, depth=num_labels, dtype=tf.compat.v1.float32)

            predicted_labels = tf.compat.v1.squeeze(
                tf.compat.v1.argmax(log_probs, axis=-1, output_type=tf.compat.v1.int32))

            if is_predicting:
                return predicted_labels, log_probs

            per_example_loss = -tf.compat.v1.reduce_sum(one_hot_labels * log_probs, axis=-1)
            loss = tf.compat.v1.reduce_mean(per_example_loss)
            return loss, predicted_labels, log_probs

    def get_loadable_object(self):
        pass

    def get_default_params(self):
        return {}

    def build_param_grid(self, params_dict):
        pass

    def get_model_params(self, model):
        pass

    @classmethod
    def train(cls, model, data, target, params_dict):
        try:
            cls.logger.info("Fitting model")
            cls.logger.debug("Data frame columns: " + str(data.columns))

            train_vectors = cls.make_train_vectors(data, params_dict)

            train_input_fn = bert.run_classifier.input_fn_builder(
                features=train_vectors,
                seq_length=params_dict[CommonConstants.MAX_SEQ_LENGTH],
                is_training=True,
                drop_remainder=False)

            trained_model = model.train(input_fn=train_input_fn, steps=params_dict[CommonConstants.NUM_TRAIN_STEPS])
            cls.logger.info("Model fitted")

            return trained_model

        except Exception as exp:
            cls.logger.error('Exception occured while training data to model : ' + str(model))
            raise CommonBaseException(exp)

    @classmethod
    def make_train_vectors(cls, data, param_dict):
        input_example = data.apply(lambda x: bert.run_classifier.InputExample(guid=None,
                                                                              text_a=x[param_dict[CommonConstants.READ_DATA_COLUMNS_TAG]],
                                                                              text_b=None,
                                                                              label=x[param_dict[CommonConstants.LABEL_COLUMN_TAG]]), axis=1)
        tokenizer = cls.create_tokenizer_from_hub_module(param_dict[CommonConstants.BERT_MODEL_HUB])
        features = bert.run_classifier.convert_examples_to_features(input_example, param_dict[CommonConstants.CLASS_LABEL],
                                                                    param_dict[CommonConstants.MAX_SEQ_LENGTH],
                                                                    tokenizer)
        return features

    @classmethod
    def create_tokenizer_from_hub_module(cls, bert_model_hub):

        with tf.compat.v1.Graph().as_default():
            bert_module = hub.Module(bert_model_hub)
            tokenization_info = bert_module(signature="tokenization_info", as_dict=True)
            with tf.compat.v1.Session() as sess:
                vocab_file, do_lower_case = sess.run([tokenization_info["vocab_file"],
                                                      tokenization_info["do_lower_case"]])

        return bert.tokenization.FullTokenizer(
            vocab_file=vocab_file, do_lower_case=do_lower_case)

    @classmethod
    def make_test_vectors(cls, data, params_dict):
        input_example = data.apply(lambda x: bert.run_classifier.InputExample(guid=None,
                                                                              text_a=x[params_dict[CommonConstants.READ_DATA_COLUMNS_TAG]],
                                                                              text_b=None,
                                                                              label=x[params_dict[CommonConstants.LABEL_COLUMN_TAG]]), axis=1)
        tokenizer = cls.create_tokenizer_from_hub_module(params_dict[CommonConstants.BERT_MODEL_HUB])
        features = bert.run_classifier.convert_examples_to_features(input_example,
                                                                    params_dict[CommonConstants.CLASS_LABEL],
                                                                    params_dict[CommonConstants.MAX_SEQ_LENGTH],
                                                                    tokenizer)
        return features

    @classmethod
    def predict(cls, model, data, params_dict):
        try:
            cls.logger.info("Testing model")
            cls.logger.debug("Data frame columns: " + str(data.columns))

            test_vectors = cls.make_test_vectors(data, params_dict)

            test_input_fn = bert.run_classifier.input_fn_builder(
                features=test_vectors,
                seq_length=params_dict[CommonConstants.MAX_SEQ_LENGTH],
                is_training=False,
                drop_remainder=False)

            result, output = model.predict(input_fn=test_input_fn)

            print('Result', result)
            print('Output', output)

            return result

        except Exception as exp:
            cls.logger.error('Exception occured while testing data to model : ' + str(model))
            raise CommonBaseException(exp)

    def perform_cross_validation(cls, model, data, target, params_dict):
        pass
