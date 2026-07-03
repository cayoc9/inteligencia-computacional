from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

from breast_cancer_survival.paths import DATASET_PATH


CANONICAL_RENAMES = {
    "reginol_node_positive": "regional_node_positive",
}

GRADE_MAP = {
    "1": 1,
    "2": 2,
    "3": 3,
    "anaplastic; grade iv": 4,
}

TARGET_MAP = {"Alive": 0, "Dead": 1}


def clean_column_name(name: str) -> str:
    cleaned = name.strip().lower()
    cleaned = re.sub(r"[^a-z0-9]+", "_", cleaned).strip("_")
    return CANONICAL_RENAMES.get(cleaned, cleaned)


def load_raw_data(path: Path = DATASET_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def _strip_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    for col in cleaned.select_dtypes(include=["object", "string"]).columns:
        cleaned[col] = cleaned[col].astype("string").str.strip()
    return cleaned


def sanitize_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = [clean_column_name(col) for col in cleaned.columns]
    cleaned = _strip_text_columns(cleaned)

    unexpected_status = set(cleaned["status"].dropna().unique()) - set(TARGET_MAP)
    if unexpected_status:
        raise ValueError(f"Unexpected status values: {sorted(unexpected_status)}")
    cleaned["status"] = cleaned["status"].map(TARGET_MAP).astype("int64")

    normalized_grade = cleaned["grade"].astype("string").str.strip().str.lower()
    unexpected_grade = set(normalized_grade.dropna().unique()) - set(GRADE_MAP)
    if unexpected_grade:
        raise ValueError(f"Unexpected grade values: {sorted(unexpected_grade)}")
    cleaned["grade"] = normalized_grade.map(GRADE_MAP).astype("int64")

    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    return cleaned


def build_dataset_contract(raw: pd.DataFrame, clean: pd.DataFrame) -> dict:
    return {
        "raw_rows": int(len(raw)),
        "clean_rows": int(len(clean)),
        "raw_columns": int(raw.shape[1]),
        "clean_columns": int(clean.shape[1]),
        "raw_duplicates": int(raw.duplicated().sum()),
        "clean_duplicates": int(clean.duplicated().sum()),
        "clean_missing_total": int(clean.isna().sum().sum()),
        "target_counts": {
            str(k): int(v) for k, v in clean["status"].value_counts().sort_index().items()
        },
        "target_rates": {
            str(k): float(v)
            for k, v in clean["status"].value_counts(normalize=True).sort_index().items()
        },
    }

