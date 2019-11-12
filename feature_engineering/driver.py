# INIT
#
#
#
# Libraries Used:
import pandas as pd
import nltk
from nltk.corpus import wordnet
from nltk.chunk import tree2conlltags
import en_core_web_sm
from textstat.textstat import textstatistics, easy_word_set


# UTILITIES:
#
#
#
# SPACY MODEL LOAD
nlp = en_core_web_sm.load()

# DATA INPUT:
#
#
#
# Call Transcripts After Feature Engineering
transcripts = pd.read_csv('../../data/Call_Transcripts_PreProcessing.csv', sep=',', encoding='utf-8')

# Call Info
calls = pd.read_csv('../../data/Call_Info.csv', sep=',', encoding='utf-8')

# Call Key Performance Indicators
kpis = pd.read_csv('../../data/Call_Key_Performance_Indicators.csv', sep=',', encoding='utf-8')

# BUSINESS LOGIC:
#
#
#
# Set Value Greater if Less Than
def setvaluegreater(num, threshold, value):
    """

    :param num:
    :param threshold:
    :param value:
    :return:
    """
    if num < threshold:
        num = value
    return num

# Set Value Less if Greater Than
def setvaluesmaller(num, threshold, value):
    """

    :param num:
    :param threshold:
    :param value:
    :return:
    """
    if num > threshold:
        num = value
    return num

# Length of An Array
def count_of_Array(arr):
    """

    :param arr:
    :return:
    """
    return len(arr)

# Number of Sentences in every Conversation Piece (All Speakers):
def num_of_sentences(text):
    """

    :param text:
    :return:
    """
    return textstatistics.sentence_count(text)

# Difference of Two Columns in Dataframe
def difference_of_cols(dfcol1, dfcol2):
    """

    :param dfcol1:
    :param dfcol2:
    :return:
    """
    return dfcol1 - dfcol2

# Dividing Two Columns in Dataframe
def dividing_cols(dfcol1, dfcol2):
    """

    :param dfcol1:
    :param dfcol2:
    :return:
    """
    return dfcol1 / dfcol2

# Multiplying Two Columns in Dataframe
def multiplying_cols(dfcol1, dfcol2):
    """

    :param dfcol1:
    :param dfcol2:
    :return:
    """
    return dfcol1*dfcol2

# Adding Columns in Dataframe
def adding_cols(dfcol1, dfcol2):
    """

    :param dfcol1:
    :param dfcol2:
    :return:
    """
    return dfcol1+dfcol2

# Number of Words in Every Conversation Piece (All Speakers):
def num_of_words(dfcol):
    """

    :param dfcol:
    :return:
    """
    numofwords = []
    for text in dfcol.as_matrix():
        stripped = text.replace("[", "").replace("]", "").replace("'", "")
        splits = stripped.split(',')
        numofwords.append(len(splits))
    return numofwords

# Total Words in Every Call By Both Speakers
def words_in_every_call_both(transcripts, callid_name, numofwords_name, row):
    """

    :param transcripts:
    :param callid_name:
    :param numofwords_name:
    :param row:
    :return:
    """
    totalwordsboth = []
    wordsboth = transcripts[numofwords_name].where(transcripts[callid_name] == row).dropna()
    convwordsboth = 0
    for convlen in wordsboth.as_matrix():
        convwordsboth += convlen
    totalwordsboth.append(convwordsboth)
    return totalwordsboth

# Words in every Call per Speaker
def words_in_every_call_speaker(transcripts, callid_name, speaker_name, numofwords_name, row, speaker):
    """

    :param transcripts:
    :param callid_name:
    :param speaker_name:
    :param numofwords_name:
    :param row:
    :param speaker:
    :return:
    """
    totalwordsspeaker = []
    maincalls = transcripts.where(transcripts[callid_name] == row).dropna()
    wordscsr = maincalls[numofwords_name].where(transcripts[speaker_name] == speaker).dropna()
    convwordscsr = 0
    for convlen in wordscsr.as_matrix():
        convwordscsr += convlen
    totalwordsspeaker.append(convwordscsr)
    return totalwordsspeaker

# Words in every Call Total (Wrapper Functions)
def words_in_every_call_all(callids, transcripts, callid_name, csr, caller, numofwords_name, speaker_name):
    """

    :param callids:
    :param transcripts:
    :param callid_name:
    :param csr:
    :param caller:
    :param numofwords_name:
    :param speaker_name:
    :return:
    """
    totalwordsboth = []
    totalwordscsr = []
    totalwordscaller = []
    for row in callids.as_matrix():
        totalwordsboth.append(words_in_every_call_both(transcripts, callid_name, numofwords_name, row))
        totalwordscsr.append(words_in_every_call_speaker(transcripts, callid_name, speaker_name, numofwords_name, row, 1))
        totalwordscaller.append(words_in_every_call_speaker(transcripts, callid_name, speaker_name, numofwords_name, row, 2))
    return totalwordsboth, totalwordscsr, totalwordscaller

# Total Words in Transcripts (Per Speaker and Collectively)
def features_in_transcripts_both(transcol, calls, feat_name, callid_name):
    """

    :param transcol:
    :param calls:
    :param feat_name:
    :param callid_name:
    :return:
    """
    feat_array = []
    for row in transcol.as_matrix():
        length = calls[feat_name].where(calls[callid_name] == row).dropna()
        feat_array.append(length.as_matrix()[0])
    return feat_array

# Parts of Speech (POS) Tags
def pos_tags_andtoks(text):
    """

    :param text:
    :return:
    """
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    return tagged

# Inside Outside Beginning (IOB) Tags
def iobtags(text):
    """

    :param text:
    :return:
    """
    return tree2conlltags(text)

# NLTK Parts of Speech Chunks
def nltk_chunks(text):
    """

    :param text:
    :return:
    """
    return nltk.ne_chunk(text)

# Text Customized Chunking
def chunking_text(reg, text):
    """

    :param reg:
    :param text:
    :return:
    """
    chunkParser = nltk.RegexpParser(reg)
    chunked = chunkParser.parse(text)
    return chunked

# SPACY Library Chunks (Comparison for NLTK)
def spacy_chunks(text):
    return [(X, X.ent_iob_, X.ent_type_) for X in nlp(text)]

# Fogg index - word difficulty_index measurement
def difficulty(text):
    """

    :param text:
    :return:
    """
    difficulties = []
    stripped = text.replace("[", "").replace("]", "").replace("'", "")
    splits = stripped.split(',')
    for word in splits:
        if word not in easy_word_set and textstatistics().syllable_count(word) > 2:
            difficulties.append(word)
    return difficulties

# Flesch Reading Ease - ease of reading
def syllables(text):
    """

    :param text:
    :return:
    """
    num_of_syllables = 0
    stripped = text.replace("[", "").replace("]", "").replace("'", "")
    splits = stripped.split(',')
    for word in splits:
        num_of_syllables += textstatistics().syllable_count(word)
    return num_of_syllables

# Smog Index Calculation
def poly_syllable_count(text):
    """

    :param text:
    :return:
    """
    count = 0
    stripped = text.replace("[", "").replace("]", "").replace("'", "")
    splits = stripped.split(',')
    for word in splits:
        syllable_count = textstatistics().syllable_count(word)
        if syllable_count >= 3:
            count += 1
    return count

# Word Synonyms
def get_synonyms(text):
    """

    :param text:
    :return:
    """
    synonyms = []
    stripped = text.replace("[", "").replace("]", "").replace("'", "")
    splits = stripped.split(',')
    for word in splits:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
    return synonyms

# Word Antonyms
def get_antonyms(text):
    """

    :param text:
    :return:
    """
    antonyms = []
    stripped = text.replace("[", "").replace("]", "").replace("'", "")
    splits = stripped.split(',')
    for word in splits:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    return antonyms


# DRIVER:
#
#
#
# num of words in transcript lemmas
transcripts['Num_of_Words'] = num_of_words(transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemma'])

# num of sentences in conversation
transcripts['Num_of_Sentences'] = transcripts['Conversation'].apply(lambda x: num_of_sentences(x))

# Duration of Every Conversation Piece
transcripts['Duration'] = difference_of_cols(transcripts['End'], transcripts['Start'])

# Words in every call (Whole) by all speakers (1 and 2)
calls['Total_Words_All_Speakers'], calls['Total_Words_CSR'], calls['Total_Words_Caller'] = words_in_every_call_all(calls['Call_ID'], transcripts, 'Call_ID', 1, 2, 'Num_of_Words', 'Speaker')

# Audio Length Per Transcript
transcripts['Audio_Length'] = features_in_transcripts_both(transcripts['Call_ID'], calls, 'Audio_Length', 'Call_ID')

# Total Words per Transcript All Speakers
transcripts['Total_Words_All_Speakers'] = features_in_transcripts_both(transcripts['Call_ID'], calls, 'Total_Words_All_Speakers', 'Call_ID')

# Total Words per Transcript by CSR
transcripts['Total_Words_CSR'] = features_in_transcripts_both(transcripts['Call_ID'], calls, 'Total_Words_CSR', 'Call_ID')

# Total Words per Transcript by Caller
transcripts['Total_Words_Caller'] = features_in_transcripts_both(transcripts['Call_ID'], calls, 'Total_Words_Caller', 'Call_ID')

# Duration Ratios per Conversation Piece
transcripts['Duration_Ratio'] = dividing_cols(transcripts['Duration'], transcripts['Audio_Length'])

# Words Ratios per Conversation Piece
transcripts['Total_Words_All_Speakers_Ratio'] = dividing_cols(transcripts['Num_of_Words'], transcripts['Total_Words_All_Speakers'])

# Words Ratio W.R.T CSR
transcripts['Total_Words_WRT_CSR_Ratio'] = dividing_cols(transcripts['Num_of_Words'], transcripts['Total_Words_CSR'])

# Words Ratio W.R.T Caller
transcripts['Total_Words_WRT_Caller_Ratio'] = dividing_cols(transcripts['Num_of_Words'], transcripts['Total_Words_Caller'])

# Standard Words Per Minute Ratio = 100 / 60
# Words per minute Ratio
transcripts['Words_Per_Minute'] = dividing_cols(transcripts['Num_of_Words'], transcripts['Duration'])
transcripts['Words_Per_Minute'] = multiplying_cols(transcripts['Words_Per_Minute'], 60)

# For Normal Conversation (Without Removing Pieces):
transcripts['Conversation_POSTags'] = transcripts['Conversation'].apply(lambda x: pos_tags_andtoks(x))

# NLTK NER Chunks (Person, GPE, etc)
transcripts['Conversation_POSTags_Chunks'] = transcripts['Conversation_POSTags'].apply(lambda x: nltk_chunks(x))

# hold times feature: Set to Zero for start of Call
transcripts['Hold_Time'] = difference_of_cols(transcripts['Start'], transcripts['End'].shift())
transcripts['Hold_Time'] = transcripts['Hold_Time'].apply(lambda x: setvaluegreater(x, 0, 0))

# Difficulty of every word
transcripts['Difficult_Words'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'].apply(lambda x: difficulty(x))

# Number of Difficult Words
transcripts['Num_of_Difficult_Words'] = transcripts['Difficult_Words'].apply(lambda x: count_of_Array(x))

# Average Sentence Length
transcripts['Average_Sentence_Length'] = dividing_cols(transcripts['Num_of_Words'], transcripts['Num_of_Sentences'])

# Fogg Index per transcript
transcripts['Fogg_Index'] = multiplying_cols(0.4, adding_cols(adding_cols(transcripts['Average_Sentence_Length'], multiplying_cols(dividing_cols(transcripts['Num_of_Difficult_Words'], transcripts['Num_of_Words']), 100)), 5))

# Number of Syllables per word
transcripts['Syllables_Per_Word'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'].apply(lambda x: syllables(x))

# Average number of syllables per transcript
transcripts['Average_Syllables_Per_Word'] = dividing_cols(transcripts['Syllables_Per_Word'], transcripts['Num_of_Words'])

# Flesch reading ease
transcripts['Flesch_Reading_Ease'] = difference_of_cols(206.835, difference_of_cols(multiplying_cols(1.015, transcripts['Average_Sentence_Length']), multiplying_cols(84.6, transcripts['Average_Syllables_Per_Word'])))

# Poly syllable count (greater than 3)
transcripts['Poly_Syllable_Count'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'].apply(lambda x: poly_syllable_count(x))

# Smog Index per transcript
transcripts['Smog_Index'] = adding_cols(multiplying_cols(1.043*0.5, multiplying_cols(30,dividing_cols(transcripts['Poly_Syllable_Count'], transcripts['Num_of_Sentences']))), 3.1291)

#  Dale–Chall Readability Score and normalization
transcripts['Dale_Chall_Readability_Score'] = multiplying_cols(0.1579, difference_of_cols(100, multiplying_cols(dividing_cols(difference_of_cols(transcripts['Num_of_Words'], transcripts['Num_of_Difficult_Words']), transcripts['Num_of_Words']), 100))) + multiplying_cols(0.0496, transcripts['Average_Sentence_Length'])
transcripts['Dale_Chall_Readability_Score'] = transcripts['Dale_Chall_Readability_Score'].apply(lambda x: setvaluesmaller(x,5,x+3.6365))

# Synonyms for every word
transcripts['Word_Synonyms'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'].apply(lambda x: get_synonyms(x))

# Antonyms for every word
transcripts['Word_Antonyms'] = transcripts['ConversationLowerJoinContractsNumsNoPunctTokensSpellLemmaNoStop'].apply(lambda x: get_antonyms(x))

# Nouns Chunks
transcripts['Nouns_IOB'] = transcripts['Conversation_POSTags_Chunks'].apply(lambda x: iobtags(chunking_text(r"""Chunk: {<NN.?>*}""",x)))

# Wh-Questions Chunks
transcripts['Wh_Questions_IOB'] = transcripts['Conversation_POSTags_Chunks'].apply(lambda x: iobtags(chunking_text(r"""Chunk: {<W.?>*}""", x)))

# Cardinals Chunks (Numbers)
transcripts['Cardinals_IOB'] = transcripts['Conversation_POSTags_Chunks'].apply(lambda x: iobtags(chunking_text(r"""Chunk: {<CD>*}""",x)))

# Pronouns Chunks
transcripts['Pronouns_IOB'] = transcripts['Conversation_POSTags_Chunks'].apply(lambda x: iobtags(chunking_text(r"""Chunk: {<PRP.?>*}""",x)))

# Spacy Chunks (comparison with NLTK Chunks)
transcripts['Spacy_Chunks'] = transcripts['Conversation'].apply(lambda x: spacy_chunks(x))


# DATA OUTPUT:
#
#
#
# Save Calls Info
calls.to_csv(r'../../data/Call_Info_FeatureEngineering.csv', index=None, header=True)

# Save Transcripts
transcripts.to_csv(r'../../data/Call_Transcripts_FeatureEngineering.csv', index=None, header=True)
