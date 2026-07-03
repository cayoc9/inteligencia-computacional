from pathlib import Path
import sys

import matplotlib.pyplot as plt
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
from breast_cancer_survival.explainability import (
    build_calibration_table,
    build_linear_coefficient_table,
    build_permutation_importance_table,
)
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import FIGURES_DIR, TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor
from breast_cancer_survival.splits import make_holdout_split


def plot_top_coefficients(coefficients: pd.DataFrame) -> None:
    top = coefficients.head(15).sort_values("coefficient")
    plt.figure(figsize=(10, 6))
    colors = ["#b91c1c" if value < 0 else "#166534" for value in top["coefficient"]]
    plt.barh(top["feature"], top["coefficient"], color=colors)
    plt.xlabel("Coeficiente")
    plt.title("Logistic Regression: top coeficientes absolutos")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "logistic_regression_top_coefficients.png", dpi=200)
    plt.close()


def plot_permutation_importance(importance: pd.DataFrame) -> None:
    top = importance.head(15).sort_values("importance_mean")
    plt.figure(figsize=(10, 6))
    plt.barh(top["feature"], top["importance_mean"], xerr=top["importance_std"], color="#1d4ed8")
    plt.xlabel("Permutation importance (PR AUC)")
    plt.title("Logistic Regression: permutation importance")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "logistic_regression_permutation_importance.png", dpi=200)
    plt.close()


def plot_calibration_curves(calibration_tables: list[pd.DataFrame]) -> None:
    plt.figure(figsize=(7, 7))
    plt.plot([0, 1], [0, 1], linestyle="--", color="black", linewidth=1, label="Perfeito")
    for table in calibration_tables:
        plt.plot(
            table["mean_predicted_probability"],
            table["observed_positive_rate"],
            marker="o",
            linewidth=2,
            label=table["model"].iloc[0],
        )
    plt.xlabel("Probabilidade media predita")
    plt.ylabel("Taxa observada de positivos")
    plt.title("Curvas de calibracao no teste")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "calibration_curves.png", dpi=200)
    plt.close()


def main():
    ensure_output_dirs()
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    split = make_holdout_split(X, y)
    registry = build_model_registry()

    logistic_pipe = Pipeline(
        [
            ("preprocessor", build_preprocessor(split.X_train)),
            ("classifier", registry["logistic_regression"]),
        ]
    )
    logistic_pipe.fit(split.X_train, split.y_train)
    logistic_test_prob = logistic_pipe.predict_proba(split.X_test)[:, 1]

    svm_pipe = Pipeline(
        [
            ("preprocessor", build_preprocessor(split.X_train)),
            ("classifier", registry["svm_calibrated"]),
        ]
    )
    svm_pipe.fit(split.X_train, split.y_train)
    svm_test_prob = svm_pipe.predict_proba(split.X_test)[:, 1]

    selected_names = ["logistic_regression", "random_forest", "extra_trees", "hist_gradient_boosting"]
    validation_probabilities = {}
    test_probabilities = {}
    for name in selected_names:
        pipe = Pipeline(
            [
                ("preprocessor", build_preprocessor(split.X_train)),
                ("classifier", registry[name]),
            ]
        )
        pipe.fit(split.X_train, split.y_train)
        validation_probabilities[name] = pipe.predict_proba(split.X_validation)[:, 1]
        test_probabilities[name] = pipe.predict_proba(split.X_test)[:, 1]

    weight_table = build_validation_weight_table(split.y_validation, validation_probabilities)
    weights = normalize_weights(dict(zip(weight_table["model"], weight_table["validation_f2"])))
    validation_ensemble_prob = weighted_average_probabilities(validation_probabilities, weights)
    _, _, validation_best = select_threshold_from_validation(split.y_validation, validation_ensemble_prob)
    ensemble_test_prob = weighted_average_probabilities(test_probabilities, weights)

    coefficients = build_linear_coefficient_table(logistic_pipe, split.X_train)
    coefficients.to_csv(TABLES_DIR / "logistic_regression_coefficients.csv", index=False)
    coefficients.head(20).to_csv(TABLES_DIR / "logistic_regression_top_coefficients.csv", index=False)

    permutation = build_permutation_importance_table(logistic_pipe, split.X_test, split.y_test)
    permutation.to_csv(TABLES_DIR / "logistic_regression_permutation_importance.csv", index=False)

    calibration_tables = [
        build_calibration_table(split.y_test, logistic_test_prob, model_name="logistic_regression"),
        build_calibration_table(split.y_test, svm_test_prob, model_name="svm_calibrated"),
        build_calibration_table(split.y_test, ensemble_test_prob, model_name="weighted_soft_voting"),
    ]
    calibration_table = pd.concat(calibration_tables, ignore_index=True)
    calibration_table.to_csv(TABLES_DIR / "calibration_curves.csv", index=False)

    calibration_summary = pd.DataFrame(
        [
            {
                "model": "logistic_regression",
                **evaluate_predictions(split.y_test, logistic_test_prob),
            },
            {
                "model": "svm_calibrated",
                **evaluate_predictions(split.y_test, svm_test_prob),
            },
            {
                "model": "weighted_soft_voting",
                "threshold_selected_on": "validation",
                "selected_threshold": float(validation_best["threshold"]),
                **evaluate_predictions(
                    split.y_test,
                    ensemble_test_prob,
                    threshold=float(validation_best["threshold"]),
                ),
            },
        ]
    )
    calibration_summary.to_csv(TABLES_DIR / "calibration_summary.csv", index=False)

    plot_top_coefficients(coefficients)
    plot_permutation_importance(permutation)
    plot_calibration_curves(calibration_tables)

    print("Explainability artifacts generated:")
    print((TABLES_DIR / "logistic_regression_top_coefficients.csv").name)
    print((TABLES_DIR / "logistic_regression_permutation_importance.csv").name)
    print((TABLES_DIR / "calibration_summary.csv").name)


if __name__ == "__main__":
    main()
