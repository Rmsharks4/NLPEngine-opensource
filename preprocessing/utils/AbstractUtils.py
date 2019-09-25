"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

"""

import abc


class AbstractUtils(metaclass=abc.ABCMeta):

    @staticmethod
    def load():
        """
        initializes static function load for Abstract Utils Class
        """
        pass
