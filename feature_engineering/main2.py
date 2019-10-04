
import pandas as pd

df = pd.read_csv('save.csv')

df['key'] = df['key'].str.replace('\d+_turn_', '')

print(df)

df.to_csv('temp.csv')
# def iterate_xml(data):
#     xml_to_dict = dict()
#     xml_to_dict[data.tag] = dict()
#     for key, value in data.attrib.items():
#         xml_to_dict[data.tag][key] = str(value)
#     if data.text is not '\n':
#         xml_to_dict[data.tag]['text'] = data.text
#     iterator = 0
#     for child in data:
#         xml_to_dict[data.tag][str(iterator)] = dict()
#         xml_to_dict[data.tag][str(iterator)] = iterate_xml(child)
#         iterator += 1
#     return xml_to_dict
#
#
# data_dict = iterate_xml(xml_data)
# data = json.dumps(data_dict)

# import pandas.io.json as pd_json
#
# data = pd_json.loads(data)
# df = pd_json.json_normalize(data)
#
# print(df)
#
# df.to_csv('save.csv')


# def flatten_json(nested_json):
#     out = {}
#
#     def flatten(x, name=''):
#         if type(x) is dict:
#             for a in x:
#                 flatten(x[a], name + a + '_')
#         elif type(x) is list:
#             i = 0
#             for a in x:
#                 flatten(a, name + str(i) + '_')
#                 i += 1
#         else:
#             out[name[:-1]] = x
#
#     flatten(nested_json)
#     return out


# series = pd.Series(flatten_json(data_dict))
# df = pd.DataFrame(series)
# df.drop(df.index[0])
# df[0] = df[0].str.replace('data_\d+_', '')
# print(df)
# df.to_csv('data.csv')

# def find(key, dictionary):
#     for k, v in dictionary.items():
#         if k == key:
#             yield v
#         elif isinstance(v, dict):
#             for result in find(key, v):
#                 yield result
#         elif isinstance(v, list):
#             for d in v:
#                 for result in find(key, d):
#                     yield result
#
#
# li = list(find('turn', data_dict))
#
# import pandas.io.json as pd_json
#
#
# datali = json.dumps(li)
# datali = pd_json.loads(datali)
# df = pd_json.json_normalize(datali)
#
# print(df)
#
# df.to_csv('save.csv')

# df = pd.DataFrame.from_dict(li)
# print(df)


