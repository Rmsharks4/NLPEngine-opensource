
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
from commons.config.AbstractConfig import AbstractConfig
from commons.config.AbstractConfigParser import AbstractConfigParser

var = ExpandContractionsDialoguePreProcessorImpl()
var.parse()

var = LowercaseDialoguePreProcessorImpl()
var.parse()

var = PorterStemmerDialoguePreProcessorImpl()
var.parse()

var = RemoveEmailsDialoguePreProcessorImpl()
var.parse()

var = RemoveNumericCharactersDialoguePreProcessorImpl()
var.parse()

var = RemovePunctuationDialoguePreProcessorImpl()
var.parse()

var = RemoveStopWordsDialoguePreProcessorImpl()
var.parse()

var = SpellCheckerDialoguePreProcessorImpl()
var.parse()

var = SplitJointWordsPreProcessorImpl()
var.parse()

var = WordNet_Lemmatizer_Dialogue_PreProcessor_Impl()
var.parse()
