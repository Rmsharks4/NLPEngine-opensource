from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class QWhDialogueActImpl(AbstractDialogueAct):

    def act(self, data):
        pass

# questions of the form: wh words what, which, who, whom, whose, when, where, how, why
# even in a fragment, its still considered a q-wh
# example:
# When do you want to return? How far is it?
# It arrives when?
# What about this handset? Who else?

