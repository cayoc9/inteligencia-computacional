from pathlib import Path
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.config import RANDOM_STATE, TEST_SIZE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.evaluation import evaluate_predictions
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor


def run_experiment(df, *, include_survival_months: bool, output_name: str) -> pd.DataFrame:
    X, y = split_features_target(df, include_survival_months=include_survival_months)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )
    rows = []
    for name, estimator in build_model_registry().items():
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(X_train)),
                ("classifier", estimator),
            ]
        )
        pipe.fit(X_train, y_train)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        rows.append(
            {
                "model": name,
                "include_survival_months": include_survival_months,
                **evaluate_predictions(y_test, y_prob),
            }
        )
    results = pd.DataFrame(rows).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    results.to_csv(TABLES_DIR / output_name, index=False)
    return results


def main():
    ensure_output_dirs()
    df = add_clinical_features(sanitize_data(load_raw_data()))

    no_leakage = run_experiment(
        df,
        include_survival_months=False,
        output_name="model_comparison_no_leakage.csv",
    )
    leakage = run_experiment(
        df,
        include_survival_months=True,
        output_name="model_comparison_with_survival_months.csv",
    )

    print("\n=== Primary experiment: no Survival Months ===")
    print(no_leakage.to_string(index=False))
    print("\n=== Sensitivity experiment: with Survival Months ===")
    print(leakage.to_string(index=False))


if __name__ == "__main__":
    main()

