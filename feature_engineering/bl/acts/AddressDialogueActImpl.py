from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
import spacy
import csv
from spacy.matcher import PhraseMatcher


class AddressDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        nlp = spacy.load('en_core_web_sm')
        matcher = PhraseMatcher(nlp.vocab)
        with open('../data/Address_Dict.csv', mode='r') as infile:
            reader = csv.reader(infile)
            greet_dict = dict((rows[0], rows[1]) for rows in reader)
        terms = greet_dict.keys()
        patterns = [nlp.make_doc(text) for text in terms]
        matcher.add("Address", None, *patterns)
        doc = nlp(args)
        matches = matcher(doc)
        output = []
        for match_id, start, end in matches:
            span = doc[start:end]
            output.append(span)
        return output
