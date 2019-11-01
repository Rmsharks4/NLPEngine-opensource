
from feature_engineering.utils.AbstractUtils import AbstractUtils


class ActsUtils(AbstractUtils):

    vb = None
    imp = None
    wdt = None
    wp = None
    wps = None
    wrb = None
    qwh = None
    qyn = None
    resp = None
    answ = None
    vbp = None
    vbd = None
    vbz = None
    md = None

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
        ActsUtils.resp = '_RESPONSE'
        ActsUtils.answ = 'ANSW'
        ActsUtils.vbp = 'VBP'
        ActsUtils.vbd = 'VBD'
        ActsUtils.vbz = 'VBZ'
        ActsUtils.md = 'MD'
