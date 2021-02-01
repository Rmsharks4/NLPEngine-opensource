# INIT
#
#
#
# Libraries Used:
import pandas as pd
import string
import nltk
import re
import csv
import numpy as np
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer


# UTILITIES:
#
#
#
# Spell Checker Library
spell = SpellChecker()

# Stop Words Corpus
stopwords = nltk.corpus.stopwords.words('english')

# Porter Stemmer
ps = nltk.PorterStemmer()

# Word Net Lemmatizer
wn = WordNetLemmatizer()

# CONTRACTIONS DICTIONARY
with open('../../data/Contractions_Dict.csv', mode='r') as infile:
    reader = csv.reader(infile)
    contractions_dict = dict((rows[0], rows[1]) for rows in reader)
contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))

# FIGURES DICTIONARY
with open('../../data/Figures_Dict.csv', mode='r') as infile:
    reader = csv.reader(infile)
    figures_dict = dict((rows[0], '#') for rows in reader)
figures_re = re.compile(r'\b(%s)\b' % '|'.join(figures_dict.keys()))

# DATA INPUT:
#
#
#
# Call Transcripts
transcripts = pd.read_csv('../../data/Call_Transcripts.csv', sep=',', encoding='utf-8')

# Call Info
calls = pd.read_csv('../../data/Call_Info.csv', sep=',', encoding='utf-8')

# BUSINESS LOGIC:
#
#
#
# Data Cleaning: Remove Punction
def remove_punctuation(text):
    """

    :param text:
    :return:
    """
    text_nopunct = "".join([char for char in text if char not in string.punctuation])
    return text_nopunct

# Data Cleaning: Remove Stop Words
def remove_stop_words(text):
    """

    :param text:
    :return:
    """
    text_nostop = [word for word in text if word not in stopwords]
    return text_nostop

# Data Cleaning: Tokenize
def tokenize(text):
    """

    :param text:
    :return:
    """
    text_tokens = re.split('\W+', text)
    return text_tokens

# Data Cleaning: Stemming
def stem(text):
    """

    :param text:
    :return:
    """
    text_stem = [ps.stem(word) for word in text]
    return text_stem

# Data Cleaning: Lemmatizing
def lemmatize(text):
    """

    :param text:
    :return:
    """
    text_lemma = [wn.lemmatize(word, pos='v') for word in text]
    return text_lemma

# Data Cleaning: Split Joint Words
def join_words(text):
    """

    :param text:
    :return:
    """
    text_join = text.replace('-', ' ')
    return text_join

# Data Cleaning: Expand Contractions
def expand_contractions(text):
    """

    :param text:
    :return:
    """
    def replace(match):
        return contractions_dict[match.group(0)]
    return contractions_re.sub(replace, text)

# Data Cleaning: Remove Figures
def remove_figures(text):
    """

    :param text:
    :return:
    """
    text = re.sub(r'\w*\d\w*', '#', text)
    text = re.sub(r'\w*@\w*\.\w*', '#', text)
    text = re.sub(r'\w*\.\w*', '#', text)
    text = re.sub(r'\w*\sdot\s\w*', '#', text)
    def replace(match):
        return figures_dict[match.group(0)]
    return figures_re.sub(replace, text)

# Data Cleaning: Spell Checking
def spell_check(text):
    """

    :param text:
    :return:
    """
    text_spell = []
    for word in text:
        text_spell.append(spell.correction(word))
    return text_spell

# Data Cleaning: Lowercase
def lowercase(text):
    """

    :param text:
    :return:
    """
    return text.lower()


# DRIVER
#
#
#
# LowerCase
transcripts['ConversationLower'] = transcripts['Conversation']\
    .apply(lambda x: lowercase(x))

# Cut Joint Words
transcripts['ConversationLowerJoin'] = transcripts['ConversationLower']\
    .apply(lambda x: join_words(x))

# Expand Contractions
transcripts['ConversationLowerJoinContracts'] = transcripts['ConversationLowerJoin']\
    .apply(lambda x: expand_contractions(x))

# Remove Numbers
transcripts['ConversationLowerJoinContractsNums'] = transcripts['ConversationLowerJoinContracts']\
    .apply(lambda x: remove_figures(x))

# Remove Punctuation
transcripts['ConversationLowerJoinContractsNumsNoPunct'] = transcripts['ConversationLowerJoinContractsNums']\
    .apply(lambda x: remove_punctuation(x))

# Remove Empty Rows and Columns
transcripts['ConversationLowerJoinContractsNumsNoPunct'] = transcripts['ConversationLowerJoinContractsNumsNoPunct']\
    .apply(lambda x: x.strip())
transcripts['ConversationLowerJoinContractsNumsNoPunct'].replace('', np.nan, inplace=True)
transcripts = transcripts.dropna(subset=['ConversationLowerJoinContractsNumsNoPunct'])

# Tokenize
transcripts['ConversationLowerJoinContractsNumsNoPunctTokens'] = transcripts['ConversationLowerJoinContractsNumsNoPunct']\
    .apply(lambda x: tokenize(x))

# Spell Check
transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpell'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokens']\
    .apply(lambda x: spell_check(x))

# Stem
transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellStem'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpell']\
    .apply(lambda x: stem(x))

# Lemmatize
transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemma'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpell']\
    .apply(lambda x: lemmatize(x))

# Remove Stop Words
transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellNoStop'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpell']\
    .apply(lambda x: remove_stop_words(x))

# Remove Stop Words
transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemma']\
    .apply(lambda x: remove_stop_words(x))

# DATA OUTPUT
#
#
#
# Store and Save All
transcripts.to_csv(r'../../data/Call_Transcripts_PreProcessing.csv', index=None, header=True)

