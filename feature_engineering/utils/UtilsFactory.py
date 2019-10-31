from feature_engineering.utils.AbstractUtils import AbstractUtils


class UtilsFactory:

    @staticmethod
    def get_utils(util_type):
        """

        :param util_type: (AbstractUtils) class name
        :return: (AbstractUtils) object else throws Exception
        """
        switcher = dict((x.__name__, x()) for x in AbstractUtils().__class__.__subclasses__())
        return switcher.get(util_type, None)
