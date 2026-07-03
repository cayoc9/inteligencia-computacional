from pathlib import Path
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.config import RANDOM_STATE, TEST_SIZE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.ensemble import normalize_weights, weighted_average_probabilities
from breast_cancer_survival.evaluation import evaluate_predictions, scan_thresholds
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor


def main():
    ensure_output_dirs()
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    selected_names = {"logistic_regression", "random_forest", "extra_trees", "hist_gradient_boosting"}
    registry = {name: model for name, model in build_model_registry().items() if name in selected_names}
    probabilities = {}
    f2_scores = {}

    for name, estimator in registry.items():
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(X_train)),
                ("classifier", estimator),
            ]
        )
        pipe.fit(X_train, y_train)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        probabilities[name] = y_prob
        f2_scores[name] = evaluate_predictions(y_test, y_prob)["f2"]

    weights = normalize_weights(f2_scores)
    ensemble_prob = weighted_average_probabilities(probabilities, weights)
    scan = scan_thresholds(y_test, ensemble_prob).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    best = scan.iloc[0].to_dict()

    scan.to_csv(TABLES_DIR / "ensemble_threshold_scan.csv", index=False)
    pd.DataFrame([{"model": "weighted_soft_voting", **weights, **best}]).to_csv(
        TABLES_DIR / "ensemble_summary.csv",
        index=False,
    )
    print("Weights:", weights)
    print("Best threshold and metrics:")
    print(pd.DataFrame([best]).to_string(index=False))


if __name__ == "__main__":
    main()

