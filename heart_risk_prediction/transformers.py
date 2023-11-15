from sklearn.base import BaseEstimator, TransformerMixin

class AlignColumnsTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, default_value=0):
        self.default_value = default_value
        self.columns = None

    def fit(self, X, y=None):
        self.columns = X.columns
        return self

    def transform(self, X):
        missing_cols = set(self.columns) - set(X.columns)
        for col in missing_cols:
            X[col] = self.default_value
        return X[self.columns]  # Reorder columns to match training data