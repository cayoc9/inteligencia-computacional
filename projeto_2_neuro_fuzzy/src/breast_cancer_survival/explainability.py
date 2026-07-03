from __future__ import annotations

import pandas as pd
from sklearn.calibration import calibration_curve
from sklearn.inspection import permutation_importance

from breast_cancer_survival.config import RANDOM_STATE


def _get_preprocessor_feature_names(preprocessor) -> list[str]:
    output_names: list[str] = []
    for name, transformer, columns in preprocessor.transformers_:
        if name == "remainder" or transformer == "drop":
            continue
        if name == "num":
            output_names.extend(list(columns))
            continue
        if name == "cat":
            one_hot = transformer.named_steps["one_hot"]
            output_names.extend(list(one_hot.get_feature_names_out(columns)))
            continue
        output_names.extend(list(columns))
    return output_names


def build_linear_coefficient_table(pipe, X_fit: pd.DataFrame) -> pd.DataFrame:
    preprocessor = pipe.named_steps["preprocessor"]
    classifier = pipe.named_steps["classifier"]
    feature_names = _get_preprocessor_feature_names(preprocessor)
    coefficients = classifier.coef_.ravel()
    return (
        pd.DataFrame(
            {
                "feature": feature_names,
                "coefficient": coefficients,
                "abs_coefficient": abs(coefficients),
            }
        )
        .sort_values("abs_coefficient", ascending=False)
        .reset_index(drop=True)
    )


def build_permutation_importance_table(
    pipe,
    X: pd.DataFrame,
    y: pd.Series,
    *,
    scoring: str = "average_precision",
    n_repeats: int = 20,
) -> pd.DataFrame:
    result = permutation_importance(
        pipe,
        X,
        y,
        scoring=scoring,
        n_repeats=n_repeats,
        random_state=RANDOM_STATE,
        n_jobs=1,
    )
    return (
        pd.DataFrame(
            {
                "feature": X.columns,
                "importance_mean": result.importances_mean,
                "importance_std": result.importances_std,
            }
        )
        .sort_values("importance_mean", ascending=False)
        .reset_index(drop=True)
    )


def build_calibration_table(
    y_true,
    y_prob,
    *,
    model_name: str,
    n_bins: int = 10,
) -> pd.DataFrame:
    frac_pos, mean_pred = calibration_curve(y_true, y_prob, n_bins=n_bins, strategy="quantile")
    return pd.DataFrame(
        {
            "model": model_name,
            "bin": list(range(1, len(frac_pos) + 1)),
            "mean_predicted_probability": mean_pred,
            "observed_positive_rate": frac_pos,
        }
    )
