from sklearn.feature_extraction.text import CountVectorizer
from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer


class SklearnCountVectorizerImpl(AbstractDialogueVectorizer):

    def vectorize_operation(self, args):
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(args)
        return vectorizer.get_feature_names(), X.toarray()
