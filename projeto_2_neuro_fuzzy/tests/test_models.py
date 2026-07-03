from breast_cancer_survival.models import build_model_registry


def test_model_registry_contains_required_tabular_models():
    registry = build_model_registry()
    expected = {
        "logistic_regression",
        "random_forest",
        "extra_trees",
        "hist_gradient_boosting",
        "gradient_boosting",
        "ada_boost",
        "svm_calibrated",
        "mlp",
    }
    assert expected <= set(registry)
