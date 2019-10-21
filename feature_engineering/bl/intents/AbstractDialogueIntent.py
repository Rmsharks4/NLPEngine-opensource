from flashtext.keyword import KeywordProcessor
import csv
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl


class AbstractDialogueIntent(StandardConfigParserImpl):

    def intent(self, args):
        kp = KeywordProcessor()
        with open('../data/intents/'+self.__class__.__name__+'.csv', mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                kp.add_keyword(row[0], row[1])
        return kp.extract_keywords(args)
