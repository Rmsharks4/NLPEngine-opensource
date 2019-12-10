
import pandas as pd

train_df = pd.read_csv('../data/altrain.csv', sep=',', encoding='utf-8', skipinitialspace=True)
labels_df = pd.read_csv('../data/allabels.csv', encoding='latin-1')

i = 1
for row in labels_df.values:
    rows = train_df.where(train_df['ConversationIDDataImpl'] == row[0])
    rows = rows.dropna()
    print(i, row[0], max(i for i, d in enumerate(rows.values)))
    i += 1
