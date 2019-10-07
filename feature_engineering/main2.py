
import pandas as pd

df = pd.read_csv('spaadia_data.csv')

# for key in df['Sp-Act'].unique():
#     rows = df.loc[df['Sp-Act'] == key]
#     rows.to_csv('../data/sp-acts/'+key+'.csv', index=None)

# for key in df['Mode'].unique():
#     if key is not None and type(key) == str:
#         rows = df.loc[df['Mode'] == key]
#         rows.to_csv('../data/modes/'+key+'.csv', index=None)

for key in df['Talk'].unique():
    if key is not None and type(key) == str:
        rows = df.loc[df['Talk'] == key]
        rows.to_csv('../data/talks/'+key+'.csv', index=None)

