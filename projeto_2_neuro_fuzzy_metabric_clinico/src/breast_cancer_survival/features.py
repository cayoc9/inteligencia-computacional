from __future__ import annotations

import pandas as pd
import numpy as np

from breast_cancer_survival.config import TARGET_COLUMN


LEAKAGE_COLUMNS = {
    "patient_id",
    "survival_months",
    "relapse_free_status_months",
    "relapse_free_status",
    "patient_s_vital_status",
}


def split_features_target(
    df: pd.DataFrame,
    *,
    include_survival_months: bool = False,
) -> tuple[pd.DataFrame, pd.Series]:
    drop_cols = [TARGET_COLUMN]
    if not include_survival_months:
        drop_cols.extend([col for col in LEAKAGE_COLUMNS if col in df.columns])
    else:
        drop_cols.extend([col for col in LEAKAGE_COLUMNS - {"survival_months"} if col in df.columns])
    X = df.drop(columns=drop_cols, errors="ignore")
    y = df[TARGET_COLUMN]
    return X, y


def _yes_no_flag(series: pd.Series, positive: str = "Yes") -> pd.Series:
    return series.astype("string").str.casefold().eq(positive.casefold()).fillna(False).astype("int64")


def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    engineered = df.copy()
    nodes = engineered["lymph_nodes_positive"].fillna(0).clip(lower=0)
    tumor_size = engineered["tumor_size"]
    grade = engineered["grade"]
    stage = engineered["stage"].fillna(engineered["stage"].median())
    mutation_count = engineered["mutation_count"].fillna(engineered["mutation_count"].median())

    engineered["node_positive_log1p"] = np.log1p(nodes)
    engineered["tumor_grade_burden"] = tumor_size * grade
    engineered["tumor_stage_burden"] = tumor_size * (1 + stage)
    engineered["node_stage_burden"] = nodes * (1 + stage)
    engineered["nottingham_grade_burden"] = engineered["npi"] * grade
    engineered["mutation_density"] = mutation_count / (tumor_size.clip(lower=1))
    engineered["large_tumor_flag"] = (tumor_size >= tumor_size.quantile(0.75)).astype("int64")
    engineered["high_node_burden_flag"] = (nodes >= nodes.quantile(0.75)).astype("int64")
    engineered["advanced_stage_flag"] = (stage >= 3).astype("int64")

    engineered["chemotherapy_flag"] = _yes_no_flag(engineered["chemotherapy"])
    engineered["hormone_therapy_flag"] = _yes_no_flag(engineered["hormone_therapy"])
    engineered["radio_therapy_flag"] = _yes_no_flag(engineered["radio_therapy"])
    engineered["treatment_count"] = (
        engineered["chemotherapy_flag"]
        + engineered["hormone_therapy_flag"]
        + engineered["radio_therapy_flag"]
    )

    engineered["triple_negative_like"] = (
        engineered["er_status"].astype("string").str.casefold().eq("negative")
        & engineered["pr_status"].astype("string").str.casefold().eq("negative")
        & engineered["her2_status"].astype("string").str.casefold().eq("negative")
    ).fillna(False).astype("int64")
    engineered["hr_positive_her2_negative"] = (
        (
            engineered["er_status"].astype("string").str.casefold().eq("positive")
            | engineered["pr_status"].astype("string").str.casefold().eq("positive")
        )
        & engineered["her2_status"].astype("string").str.casefold().eq("negative")
    ).fillna(False).astype("int64")
    engineered["receptor_profile"] = (
        "ER_" + engineered["er_status"].fillna("Unknown").astype("string")
        + "__PR_" + engineered["pr_status"].fillna("Unknown").astype("string")
        + "__HER2_" + engineered["her2_status"].fillna("Unknown").astype("string")
    )
    engineered["pam50_risk_group"] = engineered["pam50_subtype"].fillna("Unknown").replace(
        {
            "LumA": "lower_risk_luminal",
            "LumB": "higher_risk_luminal",
            "Her2": "her2_enriched",
            "Basal": "basal",
            "claudin-low": "basal_like",
            "Normal": "normal_like",
            "NC": "unknown",
        }
    )
    engineered["tumor_size_band"] = pd.cut(
        tumor_size,
        bins=[-float("inf"), 20, 50, float("inf")],
        labels=["small", "medium", "large"],
    ).astype("string")
    engineered["age_band"] = pd.cut(
        engineered["age"],
        bins=[-float("inf"), 45, 65, float("inf")],
        labels=["young", "middle", "older"],
    ).astype("string")
    return engineered
