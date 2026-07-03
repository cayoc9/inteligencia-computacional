from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

from breast_cancer_survival.paths import DATASET_PATH


TARGET_MAP = {"Living": 0, "Deceased": 1}


def clean_column_name(name: str) -> str:
    cleaned = name.strip().lower()
    cleaned = cleaned.replace("+", " plus ")
    cleaned = re.sub(r"[^a-z0-9]+", "_", cleaned).strip("_")
    return cleaned


def load_raw_data(path: Path = DATASET_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def _strip_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for col in cleaned.select_dtypes(include=["object", "string"]).columns:
        cleaned[col] = cleaned[col].astype("string").str.strip().replace({pd.NA: np.nan})
    return cleaned


def sanitize_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = [clean_column_name(col) for col in cleaned.columns]
    cleaned = _strip_text_columns(cleaned)

    cleaned = cleaned.rename(
        columns={
            "overall_survival_months": "survival_months",
            "overall_survival_status": "status",
            "age_at_diagnosis": "age",
            "neoplasm_histologic_grade": "grade",
            "lymph_nodes_examined_positive": "lymph_nodes_positive",
            "pam50_plus_claudin_low_subtype": "pam50_subtype",
            "3_gene_classifier_subtype": "three_gene_subtype",
            "nottingham_prognostic_index": "npi",
            "tumor_stage": "stage",
            "tumor_size": "tumor_size",
            "er_status": "er_status",
            "pr_status": "pr_status",
            "her2_status": "her2_status",
        }
    )

    required = ["status", "survival_months", "age", "tumor_size", "grade"]
    cleaned = cleaned.dropna(subset=required).copy()

    unexpected_status = set(cleaned["status"].dropna().unique()) - set(TARGET_MAP)
    if unexpected_status:
        raise ValueError(f"Unexpected status values: {sorted(unexpected_status)}")
    cleaned["status"] = cleaned["status"].map(TARGET_MAP).astype("int64")

    numeric_cols = [
        "age",
        "grade",
        "lymph_nodes_positive",
        "mutation_count",
        "npi",
        "survival_months",
        "relapse_free_status_months",
        "tumor_size",
        "stage",
        "cohort",
    ]
    for col in numeric_cols:
        if col in cleaned.columns:
            cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")

    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    return cleaned


def build_dataset_contract(raw: pd.DataFrame, clean: pd.DataFrame) -> dict:
    return {
        "source": "Kaggle gunesevitan/breast-cancer-metabric",
        "raw_rows": int(len(raw)),
        "clean_rows": int(len(clean)),
        "raw_columns": int(raw.shape[1]),
        "clean_columns": int(clean.shape[1]),
        "raw_duplicates": int(raw.duplicated().sum()),
        "clean_duplicates": int(clean.duplicated().sum()),
        "clean_missing_total": int(clean.isna().sum().sum()),
        "dropped_rows_without_core_outcome_or_features": int(len(raw) - len(clean)),
        "target_counts": {
            str(k): int(v) for k, v in clean["status"].value_counts().sort_index().items()
        },
        "target_rates": {
            str(k): float(v)
            for k, v in clean["status"].value_counts(normalize=True).sort_index().items()
        },
    }
