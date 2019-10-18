from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct


class DeclDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        pass

# subject before verb
# complex: more than one subject plus finite verb
# if multiple clauses have this structure and convery same intent, then its still one decl - else multiple
# adverbial clause that starts with (be)cause, if or when - also a separate decl.
# Questions like Statement + , right? / is it? are also decl
