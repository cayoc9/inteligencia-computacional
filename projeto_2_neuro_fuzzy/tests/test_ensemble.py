from breast_cancer_survival.ensemble import normalize_weights


def test_normalize_weights_uses_validation_scores():
    weights = normalize_weights({"rf": 0.6, "histgb": 0.9, "mlp": 0.3})

    assert round(sum(weights.values()), 6) == 1.0
    assert weights["histgb"] > weights["rf"] > weights["mlp"]

