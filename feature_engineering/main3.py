
import pandas as pd
import re
from lupyne import engine
from lucene import SimpleAnalyzer, Document, TermQuery, QueryParser, IndexSearcher, Term, Version

df = pd.read_csv('train-data.csv')

def testKeyword(self):
    searcher = IndexSearcher(self.directory, True)
    t = Term("isbn", "1930110995")
    query = TermQuery(t)
    scoreDocs = searcher.search(query, 50).scoreDocs
    self.assertEqual(1, len(scoreDocs), "JUnit in Action")

for text in df['Text'].unique():
    for word in re.split('[\s,]+', text):
        hit = Hit.cast_(word)
        print(hit.getScore(), ':', hit.getDocument['title'])

# for col in ['Talk', 'Polarity', 'Mode', 'Topic', 'Sp-Act']:
#     for key in df[col].unique():
#         if key is not None and type(key) == str:
#             rows = df.loc[df[col] == key]
#             rows.to_csv('data/'+col+'/'+key+'.csv', index=None)
