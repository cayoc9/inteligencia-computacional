import pandas as pd

from breast_cancer_survival.data import clean_column_name, load_raw_data, sanitize_data


def test_clean_column_name_normalizes_known_issues():
    assert clean_column_name("T Stage ") == "t_stage"
    assert clean_column_name("Reginol Node Positive") == "regional_node_positive"
    assert clean_column_name("Survival Months") == "survival_months"


def test_sanitize_data_trims_values_maps_target_and_removes_duplicate():
    raw = load_raw_data()
    cleaned = sanitize_data(raw)

    assert "t_stage" in cleaned.columns
    assert "reginol_node_positive" not in cleaned.columns
    assert "regional_node_positive" in cleaned.columns
    assert cleaned["marital_status"].str.endswith(" ").sum() == 0
    assert set(cleaned["status"].unique()) == {0, 1}
    assert cleaned.duplicated().sum() == 0
    assert len(cleaned) == len(raw.drop_duplicates())


def test_grade_is_numeric_ordered_after_sanitization():
    cleaned = sanitize_data(load_raw_data())
    assert pd.api.types.is_integer_dtype(cleaned["grade"])
    assert set(cleaned["grade"].unique()) <= {1, 2, 3, 4}

