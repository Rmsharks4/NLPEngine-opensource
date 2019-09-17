
import abc
import logging
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
from preprocessing.bl.PorterStemmerDialoguePreProcessorImpl import PorterStemmerDialoguePreProcessorImpl
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl
from preprocessing.bl.RemoveNumericCharactersDialoguePreProcessorImpl import RemoveNumericCharactersDialoguePreProcessorImpl
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.SplitJointWordsDialoguePreProcessorImpl import SplitJointWordsPreProcessorImpl
from preprocessing.bl.WordNetLemmatizerDialoguePreProcessorImpl import WordNet_Lemmatizer_Dialogue_PreProcessor_Impl


class AbstractDialoguePreProcessorFactory(metaclass=abc.ABCMeta):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingConstants.LOGGER_NAME)

    @classmethod
    def get_dialogue_preprocessor(cls, preprocessor_type):
        switcher = {
            ExpandContractionsDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_EXPAND_CONTRACTIONS,
            LowercaseDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_LOWERCASE,
            PorterStemmerDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_PORTER_STEMMER,
            RemoveEmailsDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_REMOVE_EMAILS,
            RemoveNumericCharactersDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_REMOVE_NUMERIC_CHARACTERS,
            RemovePunctuationDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_REMOVE_PUNCTUATION,
            RemoveStopWordsDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_REMOVE_STOP_WORDS,
            SpellCheckerDialoguePreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_SPELL_CHECKER,
            SplitJointWordsPreProcessorImpl(): PreProcessingConstants.PREPROCESSOR_TYPE_SPLIT_JOINT_WORDS,
            WordNet_Lemmatizer_Dialogue_PreProcessor_Impl(): PreProcessingConstants.PREPROCESSOR_TYPE_WORDNET_LEMMATIZER
        }

        return switcher.get(preprocessor_type, '')
