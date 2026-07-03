from __future__ import annotations

import pandas as pd

from breast_cancer_survival.config import TARGET_COLUMN


T_STAGE_MAP = {"T1": 1, "T2": 2, "T3": 3, "T4": 4}
N_STAGE_MAP = {"N1": 1, "N2": 2, "N3": 3}
STAGE_MAP = {"IIA": 2.1, "IIB": 2.2, "IIIA": 3.1, "IIIB": 3.2, "IIIC": 3.3}


def split_features_target(
    df: pd.DataFrame,
    *,
    include_survival_months: bool = False,
) -> tuple[pd.DataFrame, pd.Series]:
    drop_cols = [TARGET_COLUMN]
    if not include_survival_months:
        drop_cols.append("survival_months")
    X = df.drop(columns=drop_cols)
    y = df[TARGET_COLUMN]
    return X, y


def add_clinical_features(df: pd.DataFrame) -> pd.DataFrame:
    engineered = df.copy()
    examined = engineered["regional_node_examined"].clip(lower=1)
    positive = engineered["regional_node_positive"]
    tumor_size = engineered["tumor_size"]
    grade = engineered["grade"]

    engineered["node_positive_ratio"] = (positive / examined).clip(0, 1)
    engineered["advanced_stage_flag"] = engineered["6th_stage"].isin(["IIIB", "IIIC"]).astype("int64")
    engineered["hormone_receptor_negative"] = (
        (engineered["estrogen_status"] == "Negative")
        | (engineered["progesterone_status"] == "Negative")
    ).astype("int64")
    engineered["tumor_node_burden"] = tumor_size * (1 + engineered["node_positive_ratio"])
    engineered["t_stage_ord"] = engineered["t_stage"].map(T_STAGE_MAP).astype("int64")
    engineered["n_stage_ord"] = engineered["n_stage"].map(N_STAGE_MAP).astype("int64")
    engineered["stage_ord"] = engineered["6th_stage"].map(STAGE_MAP).astype("float64")
    engineered["node_density_per_grade"] = engineered["node_positive_ratio"] * grade
    engineered["tumor_grade_burden"] = tumor_size * grade
    engineered["tumor_node_stage_burden"] = tumor_size * (1 + engineered["n_stage_ord"])
    engineered["high_node_burden_flag"] = (positive >= positive.quantile(0.75)).astype("int64")
    engineered["large_tumor_flag"] = (tumor_size >= tumor_size.quantile(0.75)).astype("int64")
    engineered["triple_clinical_risk_flag"] = (
        (engineered["advanced_stage_flag"] == 1)
        & (engineered["hormone_receptor_negative"] == 1)
        & (grade >= 3)
    ).astype("int64")
    engineered["receptor_profile"] = (
        "ER_" + engineered["estrogen_status"].astype("string")
        + "__PR_" + engineered["progesterone_status"].astype("string")
    )
    engineered["tumor_size_band"] = pd.cut(
        tumor_size,
        bins=[-float("inf"), 20, 50, float("inf")],
        labels=["small", "medium", "large"],
    ).astype("string")
    engineered["node_positive_band"] = pd.cut(
        positive,
        bins=[-float("inf"), 0, 3, 9, float("inf")],
        labels=["none", "low", "moderate", "high"],
    ).astype("string")
    return engineered
