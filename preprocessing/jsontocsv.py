
import pandas as pd
import json
import io

import os
import csv

file_path = '../data/active-listening/'

arr = ['216.22/', '216.23/', '219.18/', '219.23/']

rows = []

for elem in arr:
    directory = os.fsencode(file_path+elem)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.__contains__('.txt'):
            print(filename[:17])
            # with open(file_path+elem+filename) as txt_file:
            #     lines = txt_file.readlines()
            #     txt_file.close()
            # with open(file_path+elem+filename, 'w+') as txt_file:
            #     dels = []
            #     for line in lines:
            #         if line.__contains__('***'):
            #             dels.append(line)
            #     for line in dels:
            #         lines.remove(line)
            #     print(file_path+elem+filename, lines)
            #     txt_file.writelines(lines)
            #     txt_file.close()
            # with open(file_path+elem+filename) as json_file:
            #     data = json.load(json_file)
            #     print(file_path+elem+filename)
            #     for line in data:
            #         rows.append([filename[:-4], line['speaker'], line['transcript']])

# df = pd.DataFrame(rows, columns=['Call ID', 'Speaker', 'Conversation', ])
# df.to_csv('active-listening.csv')

# file_path = '../data/calls/'
#
# directory = os.fsencode(file_path)
#
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     filename = filename[:17]
#     print(filename)
