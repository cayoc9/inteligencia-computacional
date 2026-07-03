from pathlib import Path
import sys

import pandas as pd
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.evaluation import evaluate_predictions, summarize_threshold_scenarios
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor
from breast_cancer_survival.splits import make_holdout_split


def run_experiment(df, *, include_survival_months: bool, output_name: str) -> pd.DataFrame:
    X, y = split_features_target(df, include_survival_months=include_survival_months)
    split = make_holdout_split(X, y)
    validation_rows = []
    test_rows = []
    for name, estimator in build_model_registry().items():
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(split.X_train)),
                ("classifier", estimator),
            ]
        )
        pipe.fit(split.X_train, split.y_train)

        validation_prob = pipe.predict_proba(split.X_validation)[:, 1]
        validation_scenarios = summarize_threshold_scenarios(split.y_validation, validation_prob)
        validation_scenarios.insert(0, "model", name)
        validation_scenarios.insert(1, "split", "validation")
        validation_scenarios.insert(2, "include_survival_months", include_survival_months)
        validation_scenarios.to_csv(
            TABLES_DIR / output_name.replace(".csv", f"__{name}_validation_threshold_scenarios.csv"),
            index=False,
        )
        validation_rows.append(
            {
                "model": name,
                "split": "validation",
                "include_survival_months": include_survival_months,
                **evaluate_predictions(split.y_validation, validation_prob),
            }
        )

        test_prob = pipe.predict_proba(split.X_test)[:, 1]
        test_scenarios = summarize_threshold_scenarios(split.y_test, test_prob)
        test_scenarios.insert(0, "model", name)
        test_scenarios.insert(1, "split", "test")
        test_scenarios.insert(2, "include_survival_months", include_survival_months)
        test_scenarios.to_csv(
            TABLES_DIR / output_name.replace(".csv", f"__{name}_test_threshold_scenarios.csv"),
            index=False,
        )
        test_rows.append(
            {
                "model": name,
                "split": "test",
                "include_survival_months": include_survival_months,
                **evaluate_predictions(split.y_test, test_prob),
            }
        )

    validation_results = pd.DataFrame(validation_rows).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    test_results = pd.DataFrame(test_rows).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    validation_results.to_csv(TABLES_DIR / output_name.replace(".csv", "_validation.csv"), index=False)
    test_results.to_csv(TABLES_DIR / output_name.replace(".csv", "_test.csv"), index=False)
    test_results.drop(columns=["split"]).to_csv(TABLES_DIR / output_name, index=False)
    return test_results


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
