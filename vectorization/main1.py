import pandas as pd
from vectorization.bl.tfidf.SklearnTfidfVectorizerImpl import SklearnTfidfVectorizerImpl
from vectorization.bl.count.SklearnCountVectorizerImpl import SklearnCountVectorizerImpl


df = pd.read_csv('../data/AppropriateOpening.csv', sep=',', encoding='utf-8')

output = SklearnCountVectorizerImpl().vectorize_operation(df['Dialogue'])

print(output)
