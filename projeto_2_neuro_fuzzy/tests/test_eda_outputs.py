from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.eda import (
    build_categorical_relationships,
    build_metadata_profile,
    build_numeric_relationships,
)


def test_metadata_profile_contains_leakage_and_roles():
    raw = load_raw_data()
    clean = sanitize_data(raw)
    profile = build_metadata_profile(raw, clean)

    assert "leakage_risk" in profile.columns
    survival = profile[profile["sanitized_column"] == "survival_months"].iloc[0]
    assert survival["role"] == "excluded_primary_model"
    assert "leakage" in survival["leakage_risk"]


def test_relationship_tables_include_expected_signals():
    clean = sanitize_data(load_raw_data())
    numeric = build_numeric_relationships(clean)
    categorical = build_categorical_relationships(clean)

    survival_corr = numeric[numeric["column"] == "survival_months"].iloc[0]
    assert survival_corr["pearson_corr_with_dead"] < -0.4
    assert "6th_stage" in set(categorical["column"])

