
import pandas as pd

df = pd.read_csv('train-data.csv')

for col in ['Talk', 'Polarity', 'Mode', 'Topic', 'Sp-Act']:
    for key in df[col].unique():
        if key is not None and type(key) == str:
            rows = df.loc[df[col] == key]
            rows.to_csv('data/'+col+'/'+key+'.csv', index=None)
