import abc


class AbstractService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(cls, args):
        pass