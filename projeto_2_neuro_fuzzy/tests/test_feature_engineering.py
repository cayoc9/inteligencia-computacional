from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import add_clinical_features


def test_add_clinical_features_creates_defensible_features():
    df = sanitize_data(load_raw_data())
    engineered = add_clinical_features(df)

    expected = {
        "node_positive_ratio",
        "advanced_stage_flag",
        "hormone_receptor_negative",
        "tumor_node_burden",
        "t_stage_ord",
        "n_stage_ord",
        "stage_ord",
        "node_density_per_grade",
        "tumor_grade_burden",
        "tumor_node_stage_burden",
        "receptor_profile",
        "tumor_size_band",
        "node_positive_band",
    }
    assert expected <= set(engineered.columns)
    assert engineered["node_positive_ratio"].between(0, 1).all()
    assert set(engineered["advanced_stage_flag"].unique()) <= {0, 1}
    assert set(engineered["hormone_receptor_negative"].unique()) <= {0, 1}
