from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class DmDialogueActImpl(AbstractDialogueAct):

    def act(self, data):
        pass

# a single word  / double word which stands alone as an utterance
# most discourse markers are small words such as:
# well, so, right, alright, ok, now, well um, okay then, that's cool.
