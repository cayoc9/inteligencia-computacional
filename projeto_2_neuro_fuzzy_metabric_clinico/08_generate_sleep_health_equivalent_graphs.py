from __future__ import annotations

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.inspection import permutation_importance
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    precision_recall_curve,
    roc_auc_score,
    roc_curve,
)
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.config import RANDOM_STATE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.ensemble import (
    build_validation_weight_table,
    normalize_weights,
    select_threshold_from_validation,
    weighted_average_probabilities,
)
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import FIGURES_DIR, TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor
from breast_cancer_survival.splits import make_holdout_split


sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial"],
        "axes.spines.top": False,
        "axes.spines.right": False,
    }
)

COLORS = {
    "ensemble": "#7c3aed",
    "gradient_boosting": "#166534",
    "hist_gradient_boosting": "#1d4ed8",
    "random_forest": "#0f766e",
    "logistic_regression": "#6b7280",
    "threshold_std": "#374151",
    "threshold_opt": "#b91c1c",
}

MODEL_LABELS = {
    "weighted_soft_voting": "Ensemble final",
    "gradient_boosting": "GradientBoosting",
    "hist_gradient_boosting": "HistGradientBoosting",
    "random_forest": "Random Forest",
    "logistic_regression": "Logistic Regression",
}

LEAKAGE_COLUMNS = {
    "status",
    "survival_months",
    "relapse_free_status_months",
    "relapse_free_status",
    "patient_s_vital_status",
    "patient_id",
}


def _fit_pipe(estimator, x_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    pipe = Pipeline(
        [
            ("preprocessor", build_preprocessor(x_train)),
            ("classifier", estimator),
        ]
    )
    pipe.fit(x_train, y_train)
    return pipe


def load_context() -> dict:
    ensure_output_dirs()
    clean = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(clean, include_survival_months=False)
    split = make_holdout_split(X, y)
    registry = build_model_registry()

    selected_for_display = [
        "gradient_boosting",
        "hist_gradient_boosting",
        "random_forest",
        "logistic_regression",
    ]
    selected_for_ensemble = [
        "logistic_regression",
        "random_forest",
        "extra_trees",
        "hist_gradient_boosting",
    ]
    all_needed = sorted(set(selected_for_display) | set(selected_for_ensemble))

    fitted: dict[str, Pipeline] = {}
    validation_probabilities: dict[str, np.ndarray] = {}
    test_probabilities: dict[str, np.ndarray] = {}

    for name in all_needed:
        pipe = _fit_pipe(registry[name], split.X_train, split.y_train)
        fitted[name] = pipe
        validation_probabilities[name] = pipe.predict_proba(split.X_validation)[:, 1]
        test_probabilities[name] = pipe.predict_proba(split.X_test)[:, 1]

    ensemble_validation_inputs = {name: validation_probabilities[name] for name in selected_for_ensemble}
    ensemble_test_inputs = {name: test_probabilities[name] for name in selected_for_ensemble}

    weight_table = build_validation_weight_table(split.y_validation, ensemble_validation_inputs)
    weights = normalize_weights(dict(zip(weight_table["model"], weight_table["validation_f2"])))
    validation_ensemble_prob = weighted_average_probabilities(ensemble_validation_inputs, weights)
    validation_scan, _, validation_best = select_threshold_from_validation(
        split.y_validation,
        validation_ensemble_prob,
    )
    ensemble_test_prob = weighted_average_probabilities(ensemble_test_inputs, weights)

    return {
        "clean": clean,
        "split": split,
        "fitted": fitted,
        "test_probabilities": test_probabilities,
        "validation_scan": validation_scan,
        "selected_threshold": float(validation_best["threshold"]),
        "ensemble_test_prob": ensemble_test_prob,
        "weights": weights,
        "selected_for_display": selected_for_display,
    }


def plot_age_distribution(clean: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=clean,
        x="age",
        hue="status",
        multiple="stack",
        kde=True,
        palette={0: "#4c78a8", 1: "#f58518"},
    )
    plt.title("Distribuicao de idade por status")
    plt.xlabel("Idade ao diagnostico")
    plt.ylabel("Registros")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "age_distribution_target.png")
    plt.close()


def plot_correlation_heatmap(clean: pd.DataFrame) -> None:
    numeric = clean.select_dtypes(include=["number"])
    plt.figure(figsize=(15, 10))
    sns.heatmap(numeric.corr(numeric_only=True), annot=False, cmap="coolwarm", center=0)
    plt.title("Mapa de calor de correlacao (variaveis numericas)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "correlation_heatmap.png")
    plt.close()


def plot_pam50_vs_target(clean: pd.DataFrame) -> None:
    work = clean.copy()
    work["pam50_plot"] = work["pam50_subtype"].fillna("Unknown")
    order = (
        work.groupby("pam50_plot", observed=True)["status"]
        .mean()
        .sort_values()
        .index.tolist()
    )
    ctab = pd.crosstab(work["pam50_plot"], work["status"], normalize="index") * 100
    ctab = ctab.reindex(order)
    ax = ctab.plot(
        kind="barh",
        stacked=True,
        figsize=(12, 8),
        color=["#4c78a8", "#f58518"],
    )
    ax.set_title("Percentual de obito por subtipo PAM50")
    ax.set_xlabel("Percentual (%)")
    ax.set_ylabel("Subtipo PAM50")
    ax.legend(title="Status", labels=["Living", "Deceased"])
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "pam50_vs_target.png")
    plt.close()


def plot_key_features_boxplot(clean: pd.DataFrame) -> None:
    features = [
        ("age", "Idade"),
        ("tumor_size", "Tumor Size"),
        ("npi", "Nottingham Prognostic Index"),
        ("lymph_nodes_positive", "Lymph Nodes Positive"),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    axes = axes.flatten()
    for ax, (feature, label) in zip(axes, features):
        sns.boxplot(
            data=clean,
            x="status",
            y=feature,
            hue="status",
            ax=ax,
            palette={0: "#4c78a8", 1: "#f58518"},
            legend=False,
        )
        ax.set_title(f"{label} vs status")
        ax.set_xlabel("Status (0=Living, 1=Deceased)")
        ax.set_ylabel(label)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "metabric_features_boxplot.png")
    plt.close()


def plot_metrics_comparison() -> None:
    test = pd.read_csv(TABLES_DIR / "model_comparison_no_leakage_test.csv")
    ensemble = pd.read_csv(TABLES_DIR / "ensemble_test_summary.csv")
    metrics_df = pd.concat(
        [
            test[test["model"].isin(["gradient_boosting", "hist_gradient_boosting", "random_forest", "logistic_regression"])],
            ensemble[["model", "accuracy", "balanced_accuracy", "precision", "recall", "f1", "f2", "pr_auc"]],
        ],
        ignore_index=True,
    )

    order = [
        "weighted_soft_voting",
        "gradient_boosting",
        "hist_gradient_boosting",
        "random_forest",
        "logistic_regression",
    ]
    metrics = ["accuracy", "balanced_accuracy", "precision", "recall", "f1", "f2", "pr_auc"]
    metric_labels = ["Accuracy", "Balanced\nAcc", "Precision", "Recall", "F1", "F2", "PR AUC"]
    colors = [
        COLORS["ensemble"],
        COLORS["gradient_boosting"],
        COLORS["hist_gradient_boosting"],
        COLORS["random_forest"],
        COLORS["logistic_regression"],
    ]

    fig, ax = plt.subplots(figsize=(13, 6))
    x = np.arange(len(metrics))
    width = 0.15
    for i, model in enumerate(order):
        row = metrics_df[metrics_df["model"] == model].iloc[0]
        values = [row[m] for m in metrics]
        offset = (i - len(order) / 2 + 0.5) * width
        bars = ax.bar(
            x + offset,
            values,
            width * 0.92,
            color=colors[i],
            edgecolor="white",
            linewidth=0.5,
            label=MODEL_LABELS[model],
        )
        if model == "weighted_soft_voting":
            for bar, value in zip(bars, values):
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height() + 0.008,
                    f"{value:.3f}",
                    ha="center",
                    va="bottom",
                    fontsize=7,
                    color=COLORS["ensemble"],
                    fontweight="bold",
                )

    ax.set_xticks(x)
    ax.set_xticklabels(metric_labels, fontsize=10)
    ax.set_ylim(0.45, 1.05)
    ax.set_ylabel("Valor")
    ax.set_title("Comparacao de modelos no METABRIC")
    ax.legend(loc="lower left", fontsize=9, frameon=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "comparacao_metricas.png")
    plt.close()


def plot_roc_curves(split, probabilities: dict[str, np.ndarray], ensemble_prob: np.ndarray) -> None:
    curves = {
        "weighted_soft_voting": ensemble_prob,
        "gradient_boosting": probabilities["gradient_boosting"],
        "hist_gradient_boosting": probabilities["hist_gradient_boosting"],
        "random_forest": probabilities["random_forest"],
        "logistic_regression": probabilities["logistic_regression"],
    }
    color_order = {
        "weighted_soft_voting": COLORS["ensemble"],
        "gradient_boosting": COLORS["gradient_boosting"],
        "hist_gradient_boosting": COLORS["hist_gradient_boosting"],
        "random_forest": COLORS["random_forest"],
        "logistic_regression": COLORS["logistic_regression"],
    }
    plt.figure(figsize=(8, 7))
    for name, probs in curves.items():
        fpr, tpr, _ = roc_curve(split.y_test, probs)
        plt.plot(
            fpr,
            tpr,
            linewidth=2.2 if name == "weighted_soft_voting" else 1.8,
            color=color_order[name],
            label=f"{MODEL_LABELS[name]} (AUC={roc_auc_score(split.y_test, probs):.3f})",
        )
    plt.plot([0, 1], [0, 1], "--", color="#9ca3af", linewidth=1)
    plt.xlabel("Taxa de falso positivo")
    plt.ylabel("Taxa de verdadeiro positivo")
    plt.title("Curvas ROC - METABRIC")
    plt.legend(loc="lower right", fontsize=9, frameon=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "curvas_roc.png")
    plt.close()


def plot_pr_curves(split, probabilities: dict[str, np.ndarray], ensemble_prob: np.ndarray) -> None:
    curves = {
        "weighted_soft_voting": ensemble_prob,
        "gradient_boosting": probabilities["gradient_boosting"],
        "hist_gradient_boosting": probabilities["hist_gradient_boosting"],
        "random_forest": probabilities["random_forest"],
        "logistic_regression": probabilities["logistic_regression"],
    }
    color_order = {
        "weighted_soft_voting": COLORS["ensemble"],
        "gradient_boosting": COLORS["gradient_boosting"],
        "hist_gradient_boosting": COLORS["hist_gradient_boosting"],
        "random_forest": COLORS["random_forest"],
        "logistic_regression": COLORS["logistic_regression"],
    }
    baseline = split.y_test.mean()
    plt.figure(figsize=(8, 7))
    for name, probs in curves.items():
        precision, recall, _ = precision_recall_curve(split.y_test, probs)
        plt.plot(
            recall,
            precision,
            linewidth=2.2 if name == "weighted_soft_voting" else 1.8,
            color=color_order[name],
            label=f"{MODEL_LABELS[name]} (PR AUC={average_precision_score(split.y_test, probs):.3f})",
        )
    plt.axhline(y=baseline, linestyle="--", color="#9ca3af", linewidth=1, label=f"Baseline ({baseline:.1%})")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Curvas Precision-Recall - METABRIC")
    plt.legend(loc="lower left", fontsize=9, frameon=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "curvas_pr.png")
    plt.close()


def plot_threshold_optimization(validation_scan: pd.DataFrame, selected_threshold: float) -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(validation_scan["threshold"], validation_scan["f2"], color=COLORS["ensemble"], lw=2.5, label="F2")
    plt.plot(validation_scan["threshold"], validation_scan["recall"], color="#dc2626", lw=1.5, ls="--", label="Recall")
    plt.plot(validation_scan["threshold"], validation_scan["precision"], color="#2563eb", lw=1.5, ls="--", label="Precision")

    std_row = validation_scan.loc[(validation_scan["threshold"] - 0.5).abs().idxmin()]
    opt_row = validation_scan.loc[(validation_scan["threshold"] - selected_threshold).abs().idxmin()]

    plt.axvline(x=0.5, color=COLORS["threshold_std"], linestyle=":", linewidth=1.5, alpha=0.8)
    plt.axvline(x=selected_threshold, color=COLORS["threshold_opt"], linestyle="--", linewidth=2, alpha=0.9)
    plt.annotate(
        f"Padrao 0.50\nF2={std_row['f2']:.3f}",
        xy=(0.5, std_row["f2"]),
        xytext=(0.56, std_row["f2"] - 0.09),
        fontsize=9,
        color=COLORS["threshold_std"],
        arrowprops=dict(arrowstyle="->", color=COLORS["threshold_std"], lw=1),
    )
    plt.annotate(
        f"Escolhido {selected_threshold:.2f}\nF2={opt_row['f2']:.3f}",
        xy=(selected_threshold, opt_row["f2"]),
        xytext=(0.22, min(1.0, opt_row["f2"] + 0.02)),
        fontsize=10,
        color=COLORS["threshold_opt"],
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=COLORS["threshold_opt"], lw=1.4),
    )

    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.title("Otimizacao de threshold do ensemble - METABRIC")
    plt.xlim(0.05, 0.70)
    plt.legend(loc="lower left", fontsize=9, frameon=True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "threshold_otimizacao.png")
    plt.close()


def plot_feature_importance(best_pipe: Pipeline, split) -> None:
    importance = permutation_importance(
        best_pipe,
        split.X_test,
        split.y_test,
        scoring="average_precision",
        n_repeats=10,
        random_state=RANDOM_STATE,
        n_jobs=1,
    )
    table = pd.DataFrame(
        {
            "feature": split.X_test.columns,
            "importance_mean": importance.importances_mean,
            "importance_std": importance.importances_std,
        }
    ).sort_values("importance_mean", ascending=False)

    top = table.head(12).sort_values("importance_mean")
    plt.figure(figsize=(10, 7))
    colors = [COLORS["gradient_boosting"] if value > 0 else "#9ca3af" for value in top["importance_mean"]]
    plt.barh(top["feature"], top["importance_mean"], xerr=top["importance_std"], color=colors)
    plt.xlabel("Queda no Average Precision")
    plt.title("Importancia de features - GradientBoosting")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "feature_importance.png")
    plt.close()


def plot_confusion_matrix_ensemble(y_test: pd.Series, ensemble_prob: np.ndarray, threshold: float) -> None:
    pred = (ensemble_prob >= threshold).astype(int)
    cm = confusion_matrix(y_test, pred, labels=[0, 1])
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Purples",
        cbar=False,
        xticklabels=["Previsto Living", "Previsto Deceased"],
        yticklabels=["Real Living", "Real Deceased"],
        ax=ax,
        annot_kws={"fontsize": 12, "fontweight": "bold"},
    )
    tn, fp, fn, tp = cm.ravel()
    ax.set_title(
        f"Matriz de confusao - Ensemble\nthreshold={threshold:.2f} | FP={fp} | FN={fn}",
        fontsize=12,
        fontweight="bold",
        pad=12,
    )
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "confusion_matrix_ensemble.png")
    plt.close()


def plot_single_feature_auc(clean: pd.DataFrame) -> None:
    rows = []
    y = clean["status"]
    numeric = clean.select_dtypes(include=["number"]).copy()
    for col in numeric.columns:
        if col in LEAKAGE_COLUMNS:
            continue
        series = numeric[col]
        if series.isna().all() or series.nunique(dropna=True) < 2:
            continue
        valid = series.notna() & y.notna()
        auc = roc_auc_score(y[valid], series[valid])
        rows.append({"feature": col, "auc_raw": auc, "auc_direction_adjusted": max(auc, 1 - auc)})
    table = pd.DataFrame(rows).sort_values("auc_direction_adjusted", ascending=False).head(10)
    plot_data = table.iloc[::-1]
    plt.figure(figsize=(9, 6))
    plt.barh(plot_data["feature"], plot_data["auc_direction_adjusted"], color="#0f766e")
    plt.axvline(x=0.5, color="#9ca3af", linestyle="--", linewidth=1)
    plt.xlabel("AUC ajustado por direcao")
    plt.title("Poder preditivo individual das features - METABRIC")
    plt.xlim(0.5, 1.0)
    for y_pos, value in enumerate(plot_data["auc_direction_adjusted"]):
        plt.text(value + 0.005, y_pos, f"{value:.3f}", va="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "feature_auc_individual.png")
    plt.close()


def main() -> None:
    context = load_context()
    clean = context["clean"]
    split = context["split"]
    fitted = context["fitted"]
    probabilities = context["test_probabilities"]
    validation_scan = context["validation_scan"]
    selected_threshold = context["selected_threshold"]
    ensemble_test_prob = context["ensemble_test_prob"]

    plot_age_distribution(clean)
    plot_correlation_heatmap(clean)
    plot_pam50_vs_target(clean)
    plot_key_features_boxplot(clean)
    plot_metrics_comparison()
    plot_roc_curves(split, probabilities, ensemble_test_prob)
    plot_pr_curves(split, probabilities, ensemble_test_prob)
    plot_threshold_optimization(validation_scan, selected_threshold)
    plot_feature_importance(fitted["gradient_boosting"], split)
    plot_confusion_matrix_ensemble(split.y_test, ensemble_test_prob, selected_threshold)
    plot_single_feature_auc(clean)

    generated = [
        "age_distribution_target.png",
        "correlation_heatmap.png",
        "pam50_vs_target.png",
        "metabric_features_boxplot.png",
        "comparacao_metricas.png",
        "curvas_roc.png",
        "curvas_pr.png",
        "threshold_otimizacao.png",
        "feature_importance.png",
        "confusion_matrix_ensemble.png",
        "feature_auc_individual.png",
    ]
    print("Generated METABRIC equivalent figures:")
    for name in generated:
        print(name)


if __name__ == "__main__":
    main()
