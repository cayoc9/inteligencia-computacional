from sklearn.compose import ColumnTransformer

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.preprocessing import build_preprocessor


def test_build_preprocessor_returns_column_transformer_for_mixed_data():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, _ = split_features_target(df)
    preprocessor = build_preprocessor(X)

    assert isinstance(preprocessor, ColumnTransformer)
    names = [name for name, _, _ in preprocessor.transformers]
    assert names == ["num", "cat"]

