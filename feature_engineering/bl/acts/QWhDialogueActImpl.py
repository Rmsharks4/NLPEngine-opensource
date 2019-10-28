from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class QWhDialogueActImpl(AbstractDialogueAct):

    def __init__(self):
        super().__init__()

    def act(self, args):
        for x, y in args:
            if y == 'WDT' or y == 'WP' or y == 'WP$' or y == 'WRB':
                return 'QWH'
        return None


