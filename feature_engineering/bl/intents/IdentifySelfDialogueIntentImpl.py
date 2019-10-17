from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent
import spacy
import json
from spacy.matcher import Matcher


class GreetDialogueIntentImpl(AbstractDialogueIntent):

    def intent(self, args):
        nlp = spacy.load('en_core_web_sm')
        matcher = Matcher(nlp.vocab)
        input_file = open('../data/Identify_Self_Dict.json')
        terms = json.load(input_file)
        patterns = [nlp.make_doc(text) for text in terms]
        matcher.add("Identify Self", None, *patterns)
        doc = nlp(args)
        matches = matcher(doc)
        output = []
        for match_id, start, end in matches:
            span = doc[start:end]
            output.append(span)
        return output
