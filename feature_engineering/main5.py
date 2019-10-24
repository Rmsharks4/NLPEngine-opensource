import os

dir_str = '../data/intents/'

directory = os.fsencode(dir_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    f = open('bl/intents/'+filename[:-4]+'.py', "w+")
    f.write('from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent\n\n\n')
    f.write('class '+filename[:-4]+'(AbstractDialogueIntent):\n\n')
    f.write('\tdef __init__(self):\n\t\tsuper().__init__()\n')
    f.close()
