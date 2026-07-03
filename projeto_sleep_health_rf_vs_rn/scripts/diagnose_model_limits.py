from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "sleep_health_dataset.csv"
OUT_DIR = ROOT / "reports" / "diagnostics"
OUT_DIR.mkdir(parents=True, exist_ok=True)

RANDOM_STATE = 42
DROP_COLUMNS = ["person_id", "felt_rested", "sleep_disorder_risk", "cognitive_performance_score"]


def make_preprocessor(x_frame: pd.DataFrame, scale_numeric: bool = True) -> ColumnTransformer:
    # Compatibilidade pandas 2.x: usar apenas 'object' para colunas categóricas
    categorical = x_frame.select_dtypes(include=["object"]).columns.tolist()
    numeric = x_frame.select_dtypes(include=["float64", "int64"]).columns.tolist()
    numeric_transformer = StandardScaler() if scale_numeric else "passthrough"
    return ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical),
        ]
    )


def metric_row(name: str, y_true: pd.Series, y_pred: np.ndarray, y_proba: np.ndarray) -> dict[str, float | str]:
    return {
        "modelo": name,
        "accuracy": accuracy_score(y_true, y_pred),
        "balanced_accuracy": balanced_accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "roc_auc": roc_auc_score(y_true, y_proba),
    }


def evaluate_holdout(name: str, model: Pipeline, x_train, x_test, y_train, y_test) -> tuple[dict, np.ndarray]:
    model.fit(x_train, y_train)
    proba = model.predict_proba(x_test)[:, 1]
    pred = (proba >= 0.5).astype(int)
    row = metric_row(name, y_test, pred, proba)
    row["confusion_matrix"] = confusion_matrix(y_test, pred).tolist()
    return row, proba


def threshold_scan(y_true: pd.Series, proba: np.ndarray) -> pd.DataFrame:
    rows = []
    for threshold in np.linspace(0.20, 0.80, 61):
        pred = (proba >= threshold).astype(int)
        rows.append(
            {
                "threshold": threshold,
                "accuracy": accuracy_score(y_true, pred),
                "balanced_accuracy": balanced_accuracy_score(y_true, pred),
                "precision": precision_score(y_true, pred, zero_division=0),
                "recall": recall_score(y_true, pred, zero_division=0),
                "f1": f1_score(y_true, pred, zero_division=0),
            }
        )
    return pd.DataFrame(rows)


def numeric_single_feature_auc(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    y = df["felt_rested"]
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        if col in ["person_id", "felt_rested"]:
            continue
        values = df[col]
        auc = roc_auc_score(y, values)
        rows.append({"feature": col, "auc_raw": auc, "auc_direction_adjusted": max(auc, 1 - auc)})
    return pd.DataFrame(rows).sort_values("auc_direction_adjusted", ascending=False)


def ambiguity_by_bins(df: pd.DataFrame) -> pd.DataFrame:
    work = df.copy()
    specs = {
        "sleep_quality_bin": ("sleep_quality_score", 10),
        "stress_bin": ("stress_score", 10),
        "work_hours_bin": ("work_hours_that_day", 8),
        "duration_bin": ("sleep_duration_hrs", 8),
    }
    for new_col, (source_col, q) in specs.items():
        work[new_col] = pd.qcut(work[source_col], q=q, duplicates="drop")

    group_cols = list(specs.keys())
    grouped = work.groupby(group_cols, observed=True)["felt_rested"].agg(["count", "mean"])
    grouped = grouped[grouped["count"] >= 50].copy()
    grouped["majority_rate"] = grouped["mean"].where(grouped["mean"] >= 0.5, 1 - grouped["mean"])
    grouped["minority_rate"] = 1 - grouped["majority_rate"]
    return grouped.reset_index().sort_values("minority_rate", ascending=False)


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    x = df.drop(columns=DROP_COLUMNS)
    y = df["felt_rested"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )

    majority_class = int(y.mode()[0])
    majority_pred = np.full_like(y_test, majority_class)
    majority_proba = np.full_like(y_test, y.mean(), dtype=float)

    diagnostics = {
        "dataset_shape": list(df.shape),
        "target_counts": y.value_counts().sort_index().to_dict(),
        "target_rates": y.value_counts(normalize=True).sort_index().to_dict(),
        "majority_baseline": metric_row("Classe majoritaria", y_test, majority_pred, majority_proba),
    }

    models = {
        "Logistic Regression": Pipeline(
            [
                ("preprocessor", make_preprocessor(x_train, scale_numeric=True)),
                ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", n_jobs=-1)),
            ]
        ),
        "Random Forest tuned-like": Pipeline(
            [
                ("preprocessor", make_preprocessor(x_train, scale_numeric=False)),
                (
                    "classifier",
                    RandomForestClassifier(
                        n_estimators=300,
                        max_depth=20,
                        min_samples_split=2,
                        class_weight="balanced_subsample",
                        random_state=RANDOM_STATE,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "Extra Trees": Pipeline(
            [
                ("preprocessor", make_preprocessor(x_train, scale_numeric=False)),
                (
                    "classifier",
                    ExtraTreesClassifier(
                        n_estimators=300,
                        max_depth=None,
                        min_samples_leaf=2,
                        class_weight="balanced",
                        random_state=RANDOM_STATE,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "HistGradientBoosting": Pipeline(
            [
                ("preprocessor", make_preprocessor(x_train, scale_numeric=False)),
                (
                    "classifier",
                    HistGradientBoostingClassifier(
                        learning_rate=0.06,
                        max_iter=250,
                        max_leaf_nodes=31,
                        l2_regularization=0.05,
                        random_state=RANDOM_STATE,
                    ),
                ),
            ]
        ),
    }

    holdout_rows = []
    proba_by_model = {}
    for name, model in models.items():
        row, proba = evaluate_holdout(name, model, x_train, x_test, y_train, y_test)
        holdout_rows.append(row)
        proba_by_model[name] = proba

    holdout_df = pd.DataFrame(holdout_rows).sort_values("roc_auc", ascending=False)
    holdout_df.to_csv(OUT_DIR / "holdout_model_comparison.csv", index=False)

    best_name = holdout_df.iloc[0]["modelo"]
    threshold_df = threshold_scan(y_test, proba_by_model[best_name])
    threshold_df.to_csv(OUT_DIR / "threshold_scan_best_model.csv", index=False)

    numeric_auc = numeric_single_feature_auc(df)
    numeric_auc.to_csv(OUT_DIR / "numeric_single_feature_auc.csv", index=False)

    ambiguity = ambiguity_by_bins(df)
    ambiguity.to_csv(OUT_DIR / "feature_bin_ambiguity.csv", index=False)

    cv_model = models["HistGradientBoosting"]
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    cv_result = cross_validate(
        cv_model,
        x,
        y,
        cv=cv,
        scoring=["accuracy", "balanced_accuracy", "f1", "roc_auc"],
        n_jobs=-1,
    )
    cv_summary = {
        metric: {
            "mean": float(np.mean(values)),
            "std": float(np.std(values)),
        }
        for metric, values in cv_result.items()
        if metric.startswith("test_")
    }

    # Permutation importance on a sample to keep diagnostics fast and readable.
    best_pipeline = models[best_name]
    best_pipeline.fit(x_train, y_train)
    sample = x_test.sample(n=min(4000, len(x_test)), random_state=RANDOM_STATE)
    sample_y = y_test.loc[sample.index]
    perm = permutation_importance(
        best_pipeline,
        sample,
        sample_y,
        n_repeats=5,
        random_state=RANDOM_STATE,
        scoring="roc_auc",
        n_jobs=-1,
    )
    permutation_df = pd.DataFrame(
        {
            "feature": x.columns,
            "importance_mean_auc_drop": perm.importances_mean,
            "importance_std": perm.importances_std,
        }
    ).sort_values("importance_mean_auc_drop", ascending=False)
    permutation_df.to_csv(OUT_DIR / "permutation_importance_best_model.csv", index=False)

    diagnostics["holdout_comparison"] = holdout_df.to_dict(orient="records")
    diagnostics["best_model"] = best_name
    diagnostics["best_threshold_by_f1"] = threshold_df.loc[threshold_df["f1"].idxmax()].to_dict()
    diagnostics["best_threshold_by_balanced_accuracy"] = threshold_df.loc[
        threshold_df["balanced_accuracy"].idxmax()
    ].to_dict()
    diagnostics["cv_hist_gradient_boosting"] = cv_summary
    diagnostics["top_numeric_single_feature_auc"] = numeric_auc.head(10).to_dict(orient="records")
    diagnostics["top_permutation_importance"] = permutation_df.head(12).to_dict(orient="records")
    diagnostics["ambiguity_summary"] = {
        "groups_count": int(len(ambiguity)),
        "mean_minority_rate": float(ambiguity["minority_rate"].mean()),
        "p75_minority_rate": float(ambiguity["minority_rate"].quantile(0.75)),
        "p90_minority_rate": float(ambiguity["minority_rate"].quantile(0.90)),
    }

    with (OUT_DIR / "diagnostics_summary.json").open("w", encoding="utf-8") as f:
        json.dump(diagnostics, f, indent=2, ensure_ascii=False)

    print(json.dumps(diagnostics, indent=2, ensure_ascii=False))
    print("\nClassification report do melhor modelo:")
    best_proba = proba_by_model[best_name]
    best_pred = (best_proba >= 0.5).astype(int)
    print(classification_report(y_test, best_pred))


if __name__ == "__main__":
    main()
