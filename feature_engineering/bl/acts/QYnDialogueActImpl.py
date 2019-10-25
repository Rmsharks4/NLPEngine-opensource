from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class QYnDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        if len(args) > 0:
            for x, y in args[0]:
                if y == 'AUX':
                    return True
        return False
