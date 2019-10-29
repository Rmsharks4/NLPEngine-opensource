
from feature_engineering.utils.AbstractUtils import AbstractUtils


class ActsUtils(AbstractUtils):

    vb = None
    imp = None
    wdt = None
    wp = None
    wps = None
    wrb = None
    qwh = None
    aux = None
    qyn = None

    @staticmethod
    def load():
        ActsUtils.vb = 'VB'
        ActsUtils.imp = 'IMP'
        ActsUtils.wdt = 'WDT'
        ActsUtils.wp = 'WP'
        ActsUtils.wps = 'WP$'
        ActsUtils.wrb = 'WRB'
        ActsUtils.qwh = 'QWH'
        ActsUtils.aux = 'AUX'
        ActsUtils.qyn = 'QYN'
