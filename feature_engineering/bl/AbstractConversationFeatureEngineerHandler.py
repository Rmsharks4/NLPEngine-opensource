import abc


class AbstractConversationFeatureEngineerHandler(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def perform_feature_engineering(self, args):
        """

        :param args: arguments needed for pre-processing pipeline
        """
        pass
