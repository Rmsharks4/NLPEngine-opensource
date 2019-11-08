from sklearn.feature_extraction.text import TfidfVectorizer
from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer


class SklearnTfidfVectorizerImpl(AbstractDialogueVectorizer):

    def vectorize_operation(self, args):
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(args)
        return vectorizer.get_feature_names(), X.toarray()
