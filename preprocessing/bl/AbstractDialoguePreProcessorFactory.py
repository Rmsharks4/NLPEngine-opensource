
import abc
import logging
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
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
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    @staticmethod
    def get_dialogue_preprocessor(preprocessor_type):
        switcher = {
            ExpandContractionsDialoguePreProcessorImpl.__name__: ExpandContractionsDialoguePreProcessorImpl(),
            LowercaseDialoguePreProcessorImpl.__name__: LowercaseDialoguePreProcessorImpl(),
            PorterStemmerDialoguePreProcessorImpl.__name__: PorterStemmerDialoguePreProcessorImpl(),
            RemoveEmailsDialoguePreProcessorImpl.__name__: RemoveEmailsDialoguePreProcessorImpl(),
            RemoveNumericCharactersDialoguePreProcessorImpl.__name__: RemoveNumericCharactersDialoguePreProcessorImpl(),
            RemovePunctuationDialoguePreProcessorImpl.__name__: RemovePunctuationDialoguePreProcessorImpl(),
            RemoveStopWordsDialoguePreProcessorImpl.__name__: RemoveStopWordsDialoguePreProcessorImpl(),
            SpellCheckerDialoguePreProcessorImpl.__name__: SpellCheckerDialoguePreProcessorImpl(),
            SplitJointWordsPreProcessorImpl.__name__: SplitJointWordsPreProcessorImpl(),
            WordNet_Lemmatizer_Dialogue_PreProcessor_Impl.__name__: WordNet_Lemmatizer_Dialogue_PreProcessor_Impl()
        }

        return switcher.get(preprocessor_type, '')
