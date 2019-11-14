
import pandas as pd
import json
import io
import re

import os
import csv

file_path = '../data/omaha/'

arr = ['222.155/', '222.156/', '223.155/']

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
            #         if line.__contains__('['):
            #             idx = lines.index(line)
            #             lines.remove(line)
            #             lines.insert(idx, '[')
            #         elif line.__contains__(']'):
            #             idx = lines.index(line)
            #             lines.remove(line)
            #             lines.insert(idx, ']')
            #         else:
            #             lines.remove(line)
            #     txt_file.writelines(lines)
            #     txt_file.close()
#             with open(file_path+elem+filename) as json_file:
#                 data = json.load(json_file)
#                 for line in data:
#                     rows.append(['\''+filename[:17], line['speaker'], line['transcript']])
#
# df = pd.DataFrame(rows, columns=['Call ID', 'Speaker', 'Conversation', ])
# df.to_csv('omaha.csv')

# file_path = '../../data/calls/'
#
# directory = os.fsencode(file_path)
#
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     filename = filename[:17]
#     print(filename)
