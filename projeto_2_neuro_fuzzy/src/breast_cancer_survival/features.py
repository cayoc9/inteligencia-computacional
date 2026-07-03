from __future__ import annotations

import pandas as pd

from breast_cancer_survival.config import TARGET_COLUMN


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

    engineered["node_positive_ratio"] = (positive / examined).clip(0, 1)
    engineered["advanced_stage_flag"] = engineered["6th_stage"].isin(["IIIB", "IIIC"]).astype("int64")
    engineered["hormone_receptor_negative"] = (
        (engineered["estrogen_status"] == "Negative")
        | (engineered["progesterone_status"] == "Negative")
    ).astype("int64")
    engineered["tumor_node_burden"] = engineered["tumor_size"] * (1 + engineered["node_positive_ratio"])
    return engineered

