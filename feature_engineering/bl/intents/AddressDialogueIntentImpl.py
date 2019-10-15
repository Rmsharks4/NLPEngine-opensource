from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent


class AddressDialogueIntentImpl(AbstractDialogueIntent):

    def intent(self, data):
        pass

# Sir / Mousier / Mister
# Madam / Ma'am / Madame / Miss / Missus / Lady / Ms.
# Doctor / Professor / General / Sergeant / Lieutenant / Major / Officer / Governor / Senator / Captain
# Representative / Judge / Attorney General / City Councilor / President / Vice President / Waiter
# Honey / Dear / Sweetie / Love / Darling / Babe or Baby / Pal / Buddy or Bud
# Bro / Homie / Man / Brother / Sis / Sister
# Mom / Dad / Everybody / guys / boys / girls
# ‍Aunt, Uncle, Grandma, Grandpa
