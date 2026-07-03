from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.ensemble import normalize_weights
from breast_cancer_survival.evaluation import summarize_threshold_scenarios
from breast_cancer_survival.explainability import build_calibration_table
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.fuzzy import build_fuzzy_features
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.splits import make_holdout_split


def test_metabric_sanitization_maps_target_and_required_columns():
    df = sanitize_data(load_raw_data())

    assert {"status", "survival_months", "age", "tumor_size", "grade"} <= set(df.columns)
    assert set(df["status"].unique()) <= {0, 1}
    assert len(df) > 1800


def test_metabric_feature_engineering_adds_molecular_and_treatment_features():
    df = add_clinical_features(sanitize_data(load_raw_data()))

    expected = {
        "tumor_grade_burden",
        "tumor_stage_burden",
        "node_stage_burden",
        "mutation_density",
        "treatment_count",
        "triple_negative_like",
        "hr_positive_her2_negative",
        "receptor_profile",
        "pam50_risk_group",
    }
    assert expected <= set(df.columns)
    assert df["treatment_count"].between(0, 3).all()


def test_metabric_split_excludes_identifier_and_survival_time_by_default():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)

    assert "patient_id" not in X.columns
    assert "survival_months" not in X.columns
    assert len(X) == len(y)


def test_metabric_fuzzy_features_are_bounded():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    fuzzy = build_fuzzy_features(df)

    assert fuzzy.shape[1] >= 12
    assert ((fuzzy >= 0) & (fuzzy <= 1)).all().all()


def test_metabric_models_and_threshold_scenarios_are_available():
    registry = build_model_registry()
    assert {"gradient_boosting", "hist_gradient_boosting", "random_forest"} <= set(registry)

    scenarios = summarize_threshold_scenarios([0, 0, 1, 1], [0.1, 0.2, 0.7, 0.9])
    assert {"max_f2", "max_recall", "max_clinical_utility"} <= set(scenarios["scenario"])


def test_metabric_holdout_split_creates_train_validation_test():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    split = make_holdout_split(X, y)

    assert len(split.X_train) + len(split.X_validation) + len(split.X_test) == len(X)
    assert len(split.y_train) + len(split.y_validation) + len(split.y_test) == len(y)
    assert len(split.X_validation) > 0
    assert len(split.X_test) > 0


def test_metabric_normalize_weights_and_calibration_helpers_work():
    weights = normalize_weights({"lr": 0.3, "rf": 0.6, "et": 0.1})
    assert round(sum(weights.values()), 6) == 1.0
    assert weights["rf"] > weights["lr"] > weights["et"]

    calibration = build_calibration_table([0, 0, 1, 1], [0.1, 0.2, 0.7, 0.9], model_name="demo")
    assert {"model", "bin", "mean_predicted_probability", "observed_positive_rate"} <= set(calibration.columns)
