from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import split_features_target


def test_main_feature_set_excludes_target_and_survival_months():
    df = sanitize_data(load_raw_data())
    X, y = split_features_target(df, include_survival_months=False)

    assert "status" not in X.columns
    assert "survival_months" not in X.columns
    assert y.name == "status"
    assert set(y.unique()) == {0, 1}


def test_leakage_sensitivity_can_include_survival_months_explicitly():
    df = sanitize_data(load_raw_data())
    X, _ = split_features_target(df, include_survival_months=True)

    assert "survival_months" in X.columns

