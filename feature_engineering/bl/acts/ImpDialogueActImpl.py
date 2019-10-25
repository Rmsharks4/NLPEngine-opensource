from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class ImpDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        if len(args) > 0:
            for x, y in args[0]:
                if y == 'VB':
                    return True
        return False
