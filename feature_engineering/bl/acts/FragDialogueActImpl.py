from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class FragDialogueActImpl(AbstractDialogueAct):

    def act(self, data):
        pass

# applies to C units which do not contain an independent finite clause.
# A <frag> may be:
#  a single stand alone word (e.g. Really? Today.)
#  a stand alone phrase (e.g. Sorry about that. Birmingham New Street.)
#  a non finite construction, containing an infinitive or a participle (e.g. Arriving at Euston at 9.45.)
#  a combination of structural types: e.g. Just a moment, please.
