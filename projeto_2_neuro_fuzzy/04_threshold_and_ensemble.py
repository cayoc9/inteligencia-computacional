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


def main():
    ensure_output_dirs()
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    split = make_holdout_split(X, y)

    selected_names = {"logistic_regression", "random_forest", "extra_trees", "hist_gradient_boosting"}
    registry = {name: model for name, model in build_model_registry().items() if name in selected_names}
    validation_probabilities = {}
    test_probabilities = {}

    for name, estimator in registry.items():
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(split.X_train)),
                ("classifier", estimator),
            ]
        )
        pipe.fit(split.X_train, split.y_train)
        validation_probabilities[name] = pipe.predict_proba(split.X_validation)[:, 1]
        test_probabilities[name] = pipe.predict_proba(split.X_test)[:, 1]

    weight_table = build_validation_weight_table(split.y_validation, validation_probabilities)
    weight_scores = dict(zip(weight_table["model"], weight_table["validation_f2"]))
    weights = normalize_weights(weight_scores)

    validation_ensemble_prob = weighted_average_probabilities(validation_probabilities, weights)
    validation_scan, validation_scenarios, validation_best = select_threshold_from_validation(
        split.y_validation,
        validation_ensemble_prob,
    )

    selected_threshold = float(validation_best["threshold"])
    test_ensemble_prob = weighted_average_probabilities(test_probabilities, weights)
    test_metrics = evaluate_predictions(split.y_test, test_ensemble_prob, threshold=selected_threshold)

    weight_table.assign(weight=weight_table["model"].map(weights)).to_csv(
        TABLES_DIR / "ensemble_validation_model_scores.csv",
        index=False,
    )
    validation_scan.to_csv(TABLES_DIR / "ensemble_validation_threshold_scan.csv", index=False)
    validation_scenarios.to_csv(
        TABLES_DIR / "ensemble_validation_threshold_scenarios.csv",
        index=False,
    )
    pd.DataFrame(
        [
            {
                "model": "weighted_soft_voting",
                "selection_split": "validation",
                "selection_rule": "max_f2_then_recall_then_pr_auc",
                **weights,
                **validation_best,
            }
        ]
    ).to_csv(TABLES_DIR / "ensemble_validation_summary.csv", index=False)
    pd.DataFrame(
        [
            {
                "model": "weighted_soft_voting",
                "selection_split": "validation",
                "selection_rule": "max_f2_then_recall_then_pr_auc",
                "selected_threshold": selected_threshold,
                **weights,
                **test_metrics,
            }
        ]
    ).to_csv(
        TABLES_DIR / "ensemble_test_summary.csv",
        index=False,
    )
    pd.DataFrame(
        [
            {
                "model": "weighted_soft_voting",
                "selection_split": "validation",
                "selection_rule": "max_f2_then_recall_then_pr_auc",
                "selected_threshold": selected_threshold,
                **weights,
                **test_metrics,
            }
        ]
    ).to_csv(
        TABLES_DIR / "ensemble_summary.csv",
        index=False,
    )

    print("Weights:", weights)
    print("Selected threshold from validation:", selected_threshold)
    print("Validation operating point:")
    print(pd.DataFrame([validation_best]).to_string(index=False))
    print("Test metrics with validation-selected threshold:")
    print(pd.DataFrame([test_metrics]).to_string(index=False))


if __name__ == "__main__":
    main()
