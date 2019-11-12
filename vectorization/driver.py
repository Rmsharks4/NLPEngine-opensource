# INIT
#
#
#
# Libraries Used:
import pandas as pd
from gensim.models import Word2Vec
import math


# UTILITIES:
#
#
#
# None

# DATA INPUT:
#
#
#
# Call Transcripts (After Feature Engineering)
path_vocab = "../../data/Call_Transcripts_PreProcessing.csv"
transcripts = pd.read_csv('../../data/Call_Transcripts_PreProcessing.csv', sep=',', encoding='latin1')

# Call Info
calls = pd.read_csv('../../data/Call_Info.csv', sep=',', encoding='latin1')

# BUSINESS LOGIC:
#
#
#
# LOOKUP FUNCTION
def create_lookup(dfcol):
    """

    :param dfcol:
    :return:
    """
    dictionary_lookup = {}
    idx = 0
    summations = dict()
    for text in dfcol.as_matrix():
        stripped = text.replace("[", "").replace("]", "").replace("'", "")
        splits = stripped.split(',')
        for word in splits:
            if word not in dictionary_lookup.keys():
                summations[word] = 1
                dictionary_lookup[word] = idx
                idx = idx + 1
            else:
                summations[word] = summations[word] + 1
    return dictionary_lookup

# ONE_HOT ENCODINGS
def create_one_hot_vects(dfcol):
    """

    :param dfcol:
    :return:
    """
    one_hot_vector = {}
    sentence = 0
    for text in dfcol.as_matrix():
        stripped = text.replace("[", "").replace("]", "").replace("'", "")
        splits = stripped.split(',')
        one_hot_vector[sentence] = dict()
        for key in dictionary_lookup.keys():
            if key in splits:
                one_hot_vector[sentence][key] = 1
            else:
                one_hot_vector[sentence][key] = 0
        sentence = sentence + 1
    return one_hot_vector

# TERM FREQUENCY INVERSE DOCUMENT FREQUENCIES
def create_tfidfs(dfcol):
    """

    :param dfcol:
    :return:
    """
    tfidf_vector = {}
    summations = dict()
    frequencies = 0
    for text in dfcol.as_matrix():
        stripped = text.replace("[", "").replace("]", "").replace("'", "")
        splits = stripped.split(',')
        tfidf_vector[frequencies] = dict()
        for key in dictionary_lookup.keys():
            if splits.count(key) > 0:
                tfidf_vector[frequencies][key] = splits.count(key) / len(splits) * abs(math.log(summations[key] / len(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'])))
            else:
                tfidf_vector[frequencies][key] = 0
        frequencies = frequencies + 1
    return tfidf_vector

# WORD EMBEDDINGS FORMATION
def create_embeddings(dfcol):
    """

    :param dfcol:
    :return:
    """
    corpus = []
    for text in dfcol.as_matrix():
        stripped = text.replace("[", "").replace("]", "").replace("'", "")
        splits = stripped.split(',')
        corpus.append(splits)
    model = Word2Vec(corpus,
                 min_count=1,   # Ignore words that appear less than this
                 size=200,      # Dimensionality of word embeddings
                 workers=2,     # Number of processors (parallelisation)
                 window=5,      # Context window for words during training
                 iter=30)
    return model

# DRIVER:
#
#
#
# Lookup Call
dictionary_lookup = create_lookup(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'])

# One Hot Encodings Call
one_hot_vector = create_one_hot_vects(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'])

# TFIDF Vector Call
tfidf_vector = create_tfidfs(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'])

# Word Embeddings Call
model = create_embeddings(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'])

# DATA OUTPUT:
#
#
#
# SAVE DICTIONARY
with open('../../data/Call_Transcripts_Vectorization_DictionaryLookUp.csv', 'w') as f:
    for key in dictionary_lookup.keys():
        f.write("%s,%s\n" % (key, dictionary_lookup[key]))

# SAVE ONE_HOT VECTORS
with open('../../data/Call_Transcripts_Vectorization_OneHotVector.csv', 'w') as f:
    for key in one_hot_vector[0]:
        f.write("%s," % key)
    f.write("\n")
    for keys in one_hot_vector.keys():
        for key in one_hot_vector[keys]:
            f.write("%s," % one_hot_vector[keys][key])
        f.write("\n")

# SAVE TFIDF VECTORS
with open('../../data/Call_Transcripts_Vectorization_TFIDFVector.csv', 'w') as f:
    for key in tfidf_vector[0]:
        f.write("%s," % key)
    f.write("\n")
    for keys in tfidf_vector.keys():
        for key in tfidf_vector[keys]:
            f.write("%s," % tfidf_vector[keys][key])
        f.write("\n")

# SAVE WORD2VEC MODEL
model.wv.save_word2vec_format('../../data/Call_Transcripts_Vectorization_WordEmbeddings.bin', binary=True)