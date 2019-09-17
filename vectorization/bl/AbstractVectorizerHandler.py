import abc


class AbstractVectorizerHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def perform_vectorization(self, args):
        pass
