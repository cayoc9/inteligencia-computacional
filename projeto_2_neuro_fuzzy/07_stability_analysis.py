from pathlib import Path
import sys

import pandas as pd
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.ensemble import (
    build_validation_weight_table,
    normalize_weights,
    select_threshold_from_validation,
    weighted_average_probabilities,
)
from breast_cancer_survival.evaluation import evaluate_predictions
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor
from breast_cancer_survival.splits import make_holdout_split


SEEDS = [7, 21, 42, 84, 126]


def evaluate_seed(seed: int) -> list[dict]:
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    split = make_holdout_split(X, y, random_state=seed)
    registry = build_model_registry()

    logistic_pipe = Pipeline(
        [
            ("preprocessor", build_preprocessor(split.X_train)),
            ("classifier", registry["logistic_regression"]),
        ]
    )
    logistic_pipe.fit(split.X_train, split.y_train)
    logistic_prob = logistic_pipe.predict_proba(split.X_test)[:, 1]

    selected_names = ["logistic_regression", "random_forest", "extra_trees", "hist_gradient_boosting"]
    validation_probabilities = {}
    test_probabilities = {}
    for name in selected_names:
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(split.X_train)),
                ("classifier", build_model_registry()[name]),
            ]
        )
        pipe.fit(split.X_train, split.y_train)
        validation_probabilities[name] = pipe.predict_proba(split.X_validation)[:, 1]
        test_probabilities[name] = pipe.predict_proba(split.X_test)[:, 1]

    weight_table = build_validation_weight_table(split.y_validation, validation_probabilities)
    weights = normalize_weights(dict(zip(weight_table["model"], weight_table["validation_f2"])))
    validation_ensemble_prob = weighted_average_probabilities(validation_probabilities, weights)
    _, _, validation_best = select_threshold_from_validation(split.y_validation, validation_ensemble_prob)
    selected_threshold = float(validation_best["threshold"])
    ensemble_test_prob = weighted_average_probabilities(test_probabilities, weights)

    return [
        {
            "seed": seed,
            "model": "logistic_regression",
            **evaluate_predictions(split.y_test, logistic_prob),
        },
        {
            "seed": seed,
            "model": "weighted_soft_voting",
            "threshold_selected_on": "validation",
            "selected_threshold": selected_threshold,
            **evaluate_predictions(split.y_test, ensemble_test_prob, threshold=selected_threshold),
        },
    ]


def main():
    ensure_output_dirs()
    rows = []
    for seed in SEEDS:
        rows.extend(evaluate_seed(seed))

    stability = pd.DataFrame(rows)
    stability.to_csv(TABLES_DIR / "stability_per_seed.csv", index=False)

    summary = (
        stability.groupby("model")
        .agg(
            seeds=("seed", "count"),
            accuracy_mean=("accuracy", "mean"),
            accuracy_std=("accuracy", "std"),
            precision_mean=("precision", "mean"),
            precision_std=("precision", "std"),
            recall_mean=("recall", "mean"),
            recall_std=("recall", "std"),
            f2_mean=("f2", "mean"),
            f2_std=("f2", "std"),
            pr_auc_mean=("pr_auc", "mean"),
            pr_auc_std=("pr_auc", "std"),
            false_negatives_mean=("false_negatives", "mean"),
            false_negatives_std=("false_negatives", "std"),
            false_positives_mean=("false_positives", "mean"),
            false_positives_std=("false_positives", "std"),
        )
        .reset_index()
    )
    summary.to_csv(TABLES_DIR / "stability_summary.csv", index=False)

    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
