import numpy as np
import pandas as pd

from breast_cancer_survival.fuzzy import build_fuzzy_features, trimf


def test_trimf_returns_membership_between_zero_and_one():
    values = np.array([0, 5, 10])
    result = trimf(values, [0, 5, 10])

    assert result.tolist() == [0.0, 1.0, 0.0]
    assert result.min() >= 0
    assert result.max() <= 1


def test_build_fuzzy_features_has_expected_columns():
    df = pd.DataFrame(
        {
            "age": [40],
            "tumor_size": [30],
            "regional_node_positive": [2],
        }
    )
    fuzzy = build_fuzzy_features(df)

    assert fuzzy.shape == (1, 9)
    assert "age_mid" in fuzzy.columns
    assert "nodes_few" in fuzzy.columns

