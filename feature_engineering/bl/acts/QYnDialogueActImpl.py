from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class QYnDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        pass

# Questions that initiate a yes / no response:
# Did you / Will you / Would you / Do you / Is there / Are you / Can You / Can I / May I ?
# an interrogative act recognized by the reversal of the position of subject
# and (auxiliary) verb, as in Does it matter? Are you ready yet?
