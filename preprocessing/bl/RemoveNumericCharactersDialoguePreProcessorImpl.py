
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from preprocessing.utils.FiguresDictionary import FiguresDictionary


class RemoveNumericCharactersDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = ExpandContractionsDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = FiguresDictionary.__name__

    @classmethod
    def replace(cls, match, figures_dict):
        return figures_dict[match.group(0)]

    @classmethod
    def remove_numeric_characters(cls, text, figures):
        text = figures.numbers_re.sub(figures.replace_text, text)
        return figures.figures_re.sub(cls.replace, text, figures.figures_dict)

    def preprocess_operation(self, args):
        return [self.remove_numeric_characters(args[self.config_pattern.properties.req_data],
                                               args[self.config_pattern.properties.req_args])]
