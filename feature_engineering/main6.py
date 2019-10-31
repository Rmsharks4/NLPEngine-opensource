from feature_engineering.bl.intents import *
from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import os
import csv

dir_str = '../data/intents/'
directory = os.fsencode(dir_str)


def get_intents():
    names = []
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        with open(dir_str+filename, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[1] not in names:
                    if 'RESPONSE' in row[1]:
                        names.append(row[1])
    return names


print([x.__name__ for x in AbstractDialogueIntent().__class__.__subclasses__()])
