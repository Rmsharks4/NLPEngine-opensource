import os

file_path = '../data/intents/'

rows = []

directory = os.fsencode(file_path)
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename[:-22].lower()+'_intent_type_modes')
