from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent


class ByeDialogueIntentImpl(AbstractDialogueIntent):

    def __init__(self):
        super().__init__()

# bye/goodbye/bye bye/ta ta
# au revoir/adios/cheerio/aloha/ciao/adieu/shalom/sayonara
# good night/good day
# all the best
# cheers
# see you later/around
# bless you
# later
# bon voyage/farewell
# so long/take it easy
# take care