from __future__ import annotations

import json

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from breast_cancer_survival.data import build_dataset_contract, clean_column_name
from breast_cancer_survival.paths import FIGURES_DIR, TABLES_DIR


def _sanitized_name(raw_col: str) -> str:
    return {
        "overall_survival_months": "survival_months",
        "overall_survival_status": "status",
        "age_at_diagnosis": "age",
        "neoplasm_histologic_grade": "grade",
        "lymph_nodes_examined_positive": "lymph_nodes_positive",
        "pam50_plus_claudin_low_subtype": "pam50_subtype",
        "3_gene_classifier_subtype": "three_gene_subtype",
        "nottingham_prognostic_index": "npi",
        "tumor_stage": "stage",
    }.get(clean_column_name(raw_col), clean_column_name(raw_col))


def build_metadata_profile(raw: pd.DataFrame, clean: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for raw_col in raw.columns:
        clean_col = _sanitized_name(raw_col)
        sample_values = ", ".join(raw[raw_col].dropna().astype(str).drop_duplicates().head(5).tolist())
        rows.append(
            {
                "raw_column": raw_col,
                "sanitized_column": clean_col,
                "raw_dtype": str(raw[raw_col].dtype),
                "clean_dtype": str(clean[clean_col].dtype) if clean_col in clean.columns else "dropped_or_renamed",
                "missing_count": int(raw[raw_col].isna().sum()),
                "missing_rate": float(raw[raw_col].isna().mean()),
                "unique_count": int(raw[raw_col].nunique(dropna=True)),
                "examples": sample_values,
            }
        )
    return pd.DataFrame(rows)


def build_numeric_relationships(clean: pd.DataFrame) -> pd.DataFrame:
    rows = []
    y = clean["status"]
    for col in clean.select_dtypes(include=["number"]).columns:
        if col == "status":
            continue
        corr = clean[col].corr(y)
        dead_median = clean.loc[y == 1, col].median()
        alive_median = clean.loc[y == 0, col].median()
        rows.append(
            {
                "column": col,
                "pearson_corr_with_deceased": float(corr) if pd.notna(corr) else 0.0,
                "living_median": float(alive_median) if pd.notna(alive_median) else None,
                "deceased_median": float(dead_median) if pd.notna(dead_median) else None,
                "leakage_note": "follow_up_risk" if col == "survival_months" else "",
            }
        )
    return pd.DataFrame(rows).sort_values("pearson_corr_with_deceased")


def build_categorical_relationships(clean: pd.DataFrame) -> pd.DataFrame:
    rows = []
    categorical_cols = clean.select_dtypes(include=["object", "string"]).columns
    for col in categorical_cols:
        if col == "patient_id":
            continue
        grouped = clean.groupby(col, observed=True)["status"].agg(["count", "mean"]).reset_index()
        for record in grouped.to_dict(orient="records"):
            rows.append(
                {
                    "column": col,
                    "category": record[col],
                    "count": int(record["count"]),
                    "deceased_rate": float(record["mean"]),
                    "sparse_category": bool(record["count"] < 30),
                }
            )
    return pd.DataFrame(rows).sort_values(["column", "deceased_rate"], ascending=[True, False])


def build_eda_summary(raw: pd.DataFrame, clean: pd.DataFrame) -> dict:
    contract = build_dataset_contract(raw, clean)
    numeric = build_numeric_relationships(clean)
    contract["top_numeric_deceased_correlations"] = numeric.head(8).to_dict(orient="records")
    contract["highest_missing_rates"] = (
        build_metadata_profile(raw, clean).sort_values("missing_rate", ascending=False).head(10).to_dict(orient="records")
    )
    return contract


def save_eda_outputs(raw: pd.DataFrame, clean: pd.DataFrame) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    metadata = build_metadata_profile(raw, clean)
    numeric = build_numeric_relationships(clean)
    categorical = build_categorical_relationships(clean)
    summary = build_eda_summary(raw, clean)

    metadata.to_csv(TABLES_DIR / "metadata_profile.csv", index=False)
    numeric.to_csv(TABLES_DIR / "numeric_relationships.csv", index=False)
    categorical.to_csv(TABLES_DIR / "categorical_relationships.csv", index=False)
    (TABLES_DIR / "data_quality_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    ax = clean["status"].value_counts().sort_index().plot(kind="bar", color=["#4c78a8", "#f58518"])
    ax.set_title("Distribuicao do alvo")
    ax.set_xlabel("Status: 0=Living, 1=Deceased")
    ax.set_ylabel("Registros")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "target_distribution.png", dpi=150)
    plt.close()

    sns.boxplot(data=clean, x="status", y="survival_months")
    plt.title("Overall Survival Months por Status")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "survival_months_by_status.png", dpi=150)
    plt.close()

    corr = clean.select_dtypes(include=["number"]).corr(numeric_only=True)
    sns.heatmap(corr, cmap="vlag", center=0)
    plt.title("Correlacao numerica")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "numeric_correlation_heatmap.png", dpi=150)
    plt.close()

    if "pam50_subtype" in clean.columns:
        pam50 = clean.groupby("pam50_subtype", observed=True)["status"].mean().sort_values()
        pam50.plot(kind="barh", color="#72b7b2")
        plt.title("Taxa de obito por subtipo PAM50")
        plt.xlabel("Deceased rate")
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / "pam50_deceased_rate.png", dpi=150)
        plt.close()

    sns.scatterplot(
        data=clean,
        x="tumor_size",
        y="lymph_nodes_positive",
        hue="status",
        alpha=0.45,
        palette={0: "#4c78a8", 1: "#f58518"},
    )
    plt.title("Tumor Size vs Positive Lymph Nodes")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "tumor_nodes_relationship.png", dpi=150)
    plt.close()
