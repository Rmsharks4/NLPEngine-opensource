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


def warn(*args, **kwargs):
    pass


warnings.warn = warn
warnings.filterwarnings("ignore")


def create_tokenizer_from_hub_module(bert_model_hub):

    with tf.compat.v1.Graph().as_default():
        bert_module = hub.Module(bert_model_hub)
        tokenization_info = bert_module(signature="tokenization_info", as_dict=True)
        with tf.compat.v1.Session() as sess:
            vocab_file, do_lower_case = sess.run([tokenization_info["vocab_file"],
                                                  tokenization_info["do_lower_case"]])

    return bert.tokenization.FullTokenizer(
        vocab_file=vocab_file, do_lower_case=do_lower_case)


def make_features(dataset, label_list, MAX_SEQ_LENGTH, tokenizer, DATA_COLUMN, LABEL_COLUMN):
    input_example = dataset.apply(lambda x: bert.run_classifier.InputExample(guid=None,
                                                                   text_a = x[DATA_COLUMN],
                                                                   text_b = None,
                                                                   label = x[LABEL_COLUMN]), axis = 1)
    features = bert.run_classifier.convert_examples_to_features(input_example, label_list, MAX_SEQ_LENGTH, tokenizer)
    return features


def create_model(bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, labels,
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

    # Use "pooled_output" for classification tasks on an entire sentence.
    # Use "sequence_outputs" for token-level output.
    output_layer = bert_outputs["pooled_output"]

    hidden_size = output_layer.shape[-1].value

    # Create our own layer to tune for politeness data.
    output_weights = tf.compat.v1.get_variable(
        "output_weights", [num_labels, hidden_size],
        initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.02))

    output_bias = tf.compat.v1.get_variable(
        "output_bias", [num_labels], initializer=tf.compat.v1.zeros_initializer())

    with tf.compat.v1.variable_scope("loss"):

        # Dropout helps prevent overfitting
        output_layer = tf.compat.v1.nn.dropout(output_layer, keep_prob=0.9)

        logits = tf.compat.v1.matmul(output_layer, output_weights, transpose_b=True)
        logits = tf.compat.v1.nn.bias_add(logits, output_bias)
        log_probs = tf.compat.v1.nn.log_softmax(logits, axis=-1)

        # Convert labels into one-hot encoding
        one_hot_labels = tf.compat.v1.one_hot(labels, depth=num_labels, dtype=tf.compat.v1.float32)

        predicted_labels = tf.compat.v1.squeeze(tf.compat.v1.argmax(log_probs, axis=-1, output_type=tf.compat.v1.int32))
        # If we're predicting, we want predicted labels and the probabiltiies.
        if is_predicting:
            return predicted_labels, log_probs

        # If we're train/eval, compute loss between predicted and actual label
        per_example_loss = -tf.compat.v1.reduce_sum(one_hot_labels * log_probs, axis=-1)
        loss = tf.compat.v1.reduce_mean(per_example_loss)
        return loss, predicted_labels, log_probs


def model_fn_builder(bert_model_hub, num_labels, learning_rate, num_train_steps,
                     num_warmup_steps):

    def model_fn(features, labels, mode, params):  # pylint: disable=unused-argument

        input_ids = features["input_ids"]
        input_mask = features["input_mask"]
        segment_ids = features["segment_ids"]
        label_ids = features["label_ids"]

        is_predicting = (mode == tf.compat.v1.estimator.ModeKeys.PREDICT)

        # TRAIN and EVAL
        if not is_predicting:

            (loss, predicted_labels, log_probs) = create_model(
                bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, label_ids, num_labels)

            train_op = bert.optimization.create_optimizer(
                loss, learning_rate, num_train_steps, num_warmup_steps, use_tpu=False)

            # Calculate evaluation metrics.
            def metric_fn(label_ids, predicted_labels):
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

            eval_metrics = metric_fn(label_ids, predicted_labels)

            if mode == tf.compat.v1.estimator.ModeKeys.TRAIN:
                return tf.compat.v1.estimator.EstimatorSpec(mode=mode,
                                                  loss=loss,
                                                  train_op=train_op)
            else:
                return tf.compat.v1.estimator.EstimatorSpec(mode=mode,
                                                  loss=loss,
                                                  eval_metric_ops=eval_metrics)
        else:
            (predicted_labels, log_probs) = create_model(
                bert_model_hub, is_predicting, input_ids, input_mask, segment_ids, label_ids, num_labels)

            predictions = {
                'probabilities': log_probs,
                'labels': predicted_labels
            }

            return tf.compat.v1.estimator.EstimatorSpec(mode, predictions=predictions)

    # Return the actual model function in the closure
    return model_fn


def estimator_builder(bert_model_hub, OUTPUT_DIR, SAVE_SUMMARY_STEPS, SAVE_CHECKPOINTS_STEPS, label_list, LEARNING_RATE,
                      num_train_steps, num_warmup_steps, BATCH_SIZE):
    # Specify outpit directory and number of checkpoint steps to save
    run_config = tf.compat.v1.estimator.RunConfig(
        model_dir=OUTPUT_DIR,
        save_summary_steps=SAVE_SUMMARY_STEPS,
        save_checkpoints_steps=SAVE_CHECKPOINTS_STEPS)

    model_fn = model_fn_builder(
        bert_model_hub=bert_model_hub,
        num_labels=len(label_list),
        learning_rate=LEARNING_RATE,
        num_train_steps=num_train_steps,
        num_warmup_steps=num_warmup_steps)

    estimator = tf.compat.v1.estimator.Estimator(
        model_fn=model_fn,
        config=run_config,
        params={"batch_size": BATCH_SIZE})
    return estimator, model_fn, run_config


OUTPUT_DIR = '/results/MY_BERT'

def run_on_dfs(train, test, DATA_COLUMNS, LABEL_COLUMNS,
               MAX_SEQ_LENGTH=128,
               BATCH_SIZE=64,
               LEARNING_RATE=2e-5,
               NUM_TRAIN_EPOCHS=1.0,
               WARMUP_PROPORTION=0.1,
               SAVE_SUMMARY_STEPS=100,
               SAVE_CHECKPOINTS_STEPS=10000,
               bert_model_hub="https://tfhub.dev/google/bert_uncased_L-12_H-768_A-12/1"):
    label_list = train[LABEL_COLUMNS].unique().tolist()

    print('RUN ON DFS')

    tokenizer = create_tokenizer_from_hub_module(bert_model_hub)

    print('LOAD TOKENIZER')

    train_features = make_features(train, label_list, MAX_SEQ_LENGTH, tokenizer, DATA_COLUMNS, LABEL_COLUMNS)
    test_features = make_features(test, label_list, MAX_SEQ_LENGTH, tokenizer, DATA_COLUMNS, LABEL_COLUMNS)

    print('TRAIN TEST SPLIT')

    num_train_steps = int(len(train_features) / BATCH_SIZE * NUM_TRAIN_EPOCHS)
    num_warmup_steps = int(num_train_steps * WARMUP_PROPORTION)

    print('num_train_steps')

    estimator, model_fn, run_config = estimator_builder(
        bert_model_hub,
        OUTPUT_DIR,
        SAVE_SUMMARY_STEPS,
        SAVE_CHECKPOINTS_STEPS,
        label_list,
        LEARNING_RATE,
        num_train_steps,
        num_warmup_steps,
        BATCH_SIZE)

    print('BUILD ESTIMATOR')

    train_input_fn = bert.run_classifier.input_fn_builder(
        features=train_features,
        seq_length=MAX_SEQ_LENGTH,
        is_training=True,
        drop_remainder=False)

    print('RUN CLASSIFIER')

    estimator.train(input_fn=train_input_fn, max_steps=num_train_steps)

    print('TRAIN ESTIMATOR')

    test_input_fn = run_classifier.input_fn_builder(
        features=test_features,
        seq_length=MAX_SEQ_LENGTH,
        is_training=False,
        drop_remainder=False)

    print('INPUT BUILDER')

    result_dict = estimator.evaluate(input_fn=test_input_fn, steps=None)

    print('EVALUATE ESTIMATOR')

    return result_dict, estimator


train_df = pd.read_csv('../data/altrain.csv', encoding='latin1')
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin1')

final = list()

for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    # vals = list()
    # for val in rows.values:
    #     vals.append([val[1], val[4]])
    # final.append([row[0], vals, row[15]])
    for val in rows.values:
        if row[15] == 'Mastered':
            final.append([row[0], str(val[4]), 1])
        else:
            final.append([row[0], str(val[4]), 0])

mid_df = pd.DataFrame(final, index=None, columns=['ConversationIDDataImpl', 'PlainTextDataImpl',
                                                      'Actively_listened_and_acknowledged_concerns'])

train, test = train_test_split(mid_df, test_size=0.2)

myparam = {
        "DATA_COLUMNS": "PlainTextDataImpl",
        "LABEL_COLUMNS": "Actively_listened_and_acknowledged_concerns",
        "LEARNING_RATE": 2e-5,
        "NUM_TRAIN_EPOCHS": 1
    }

result, estimator = run_on_dfs(train, test, **myparam)

def pretty_print(result):
    df = pd.DataFrame([result]).T
    df.columns = ["values"]
    return df


print(pretty_print(result))


def serving_input_receiver_fn():
    MAX_SEQ_LENGTH = 128

    feature_spec = {
      "input_ids": tf.FixedLenFeature([MAX_SEQ_LENGTH], tf.int64),
      "input_mask": tf.FixedLenFeature([MAX_SEQ_LENGTH], tf.int64),
      "segment_ids": tf.FixedLenFeature([MAX_SEQ_LENGTH], tf.int64),
      "label_ids":  tf.FixedLenFeature([], tf.int64)
    }

    serialized_tf_example = tf.placeholder(dtype=tf.string,
                                           shape=[None],
                                           name='input_example_tensor')

    receiver_tensors = {'example': serialized_tf_example}
    features = tf.parse_example(serialized_tf_example, feature_spec)
    return tf.estimator.export.ServingInputReceiver(features, receiver_tensors)


export_path = '/bertmodels'
estimator._export_to_tpu = False
estimator.export_saved_model(export_dir_base=export_path, serving_input_receiver_fn=serving_input_receiver_fn)

