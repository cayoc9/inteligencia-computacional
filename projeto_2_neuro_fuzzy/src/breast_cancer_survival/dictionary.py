from __future__ import annotations

import pandas as pd

from breast_cancer_survival.data import clean_column_name


RAW_COLUMN_NOTES = {
    "Age": ("age", "Patient age at diagnosis", "feature", "none"),
    "Race": ("race", "Race category", "feature", "none"),
    "Marital Status": ("marital_status", "Marital status", "feature", "none"),
    "T Stage ": ("t_stage", "Tumor stage category", "feature", "none"),
    "N Stage": ("n_stage", "Nodal stage category", "feature", "none"),
    "6th Stage": ("6th_stage", "AJCC 6th stage grouping", "feature", "none"),
    "differentiate": ("differentiate", "Tumor differentiation", "feature", "none"),
    "Grade": ("grade", "Tumor grade, ordinal 1-4 after sanitation", "feature", "none"),
    "A Stage": ("a_stage", "Regional or distant stage", "feature", "none"),
    "Tumor Size": ("tumor_size", "Tumor size", "feature", "none"),
    "Estrogen Status": ("estrogen_status", "Estrogen receptor status", "feature", "none"),
    "Progesterone Status": ("progesterone_status", "Progesterone receptor status", "feature", "none"),
    "Regional Node Examined": ("regional_node_examined", "Number of regional nodes examined", "feature", "none"),
    "Reginol Node Positive": ("regional_node_positive", "Number of positive regional nodes", "feature", "none"),
    "Survival Months": (
        "survival_months",
        "Follow-up survival time in months",
        "excluded_primary_model",
        "leakage/follow_up_risk",
    ),
    "Status": ("status", "Survival status: Alive=0, Dead=1", "target", "none"),
}

DERIVED_FEATURES = [
    {
        "raw_column": "",
        "sanitized_column": "node_positive_ratio",
        "raw_dtype": "derived",
        "clean_dtype": "float64",
        "role": "derived_feature",
        "leakage_risk": "none",
        "description": "regional_node_positive / regional_node_examined, clipped to 0-1",
        "domain_or_examples": "0.0-1.0",
    },
    {
        "raw_column": "",
        "sanitized_column": "advanced_stage_flag",
        "raw_dtype": "derived",
        "clean_dtype": "int64",
        "role": "derived_feature",
        "leakage_risk": "none",
        "description": "1 when 6th_stage is IIIB or IIIC, else 0",
        "domain_or_examples": "0, 1",
    },
    {
        "raw_column": "",
        "sanitized_column": "hormone_receptor_negative",
        "raw_dtype": "derived",
        "clean_dtype": "int64",
        "role": "derived_feature",
        "leakage_risk": "none",
        "description": "1 when estrogen or progesterone status is Negative",
        "domain_or_examples": "0, 1",
    },
    {
        "raw_column": "",
        "sanitized_column": "tumor_node_burden",
        "raw_dtype": "derived",
        "clean_dtype": "float64",
        "role": "derived_feature",
        "leakage_risk": "none",
        "description": "tumor_size * (1 + node_positive_ratio)",
        "domain_or_examples": "positive numeric",
    },
]


def _examples(series: pd.Series, limit: int = 6) -> str:
    values = series.dropna().astype(str).drop_duplicates().head(limit).tolist()
    return ", ".join(values)


def build_data_dictionary(raw: pd.DataFrame, clean: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for raw_col in raw.columns:
        sanitized_col = clean_column_name(raw_col)
        expected_sanitized, description, role, leakage = RAW_COLUMN_NOTES[raw_col]
        if sanitized_col != expected_sanitized:
            sanitized_col = expected_sanitized
        rows.append(
            {
                "raw_column": raw_col,
                "sanitized_column": sanitized_col,
                "raw_dtype": str(raw[raw_col].dtype),
                "clean_dtype": str(clean[sanitized_col].dtype),
                "role": role,
                "leakage_risk": leakage,
                "description": description,
                "domain_or_examples": _examples(raw[raw_col]),
            }
        )
    rows.extend(DERIVED_FEATURES)
    return pd.DataFrame(rows)


def write_data_dictionary(dictionary: pd.DataFrame, path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Dicionario de Dados: Projeto 2 Breast Cancer",
        "",
        "Este dicionario cobre o CSV bruto, os nomes sanitizados, papeis analiticos, risco de vazamento e features derivadas.",
        "",
        "| Raw column | Sanitized column | Raw dtype | Clean dtype | Role | Leakage risk | Description | Domain/examples |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in dictionary.to_dict(orient="records"):
        lines.append(
            "| {raw_column} | {sanitized_column} | {raw_dtype} | {clean_dtype} | {role} | {leakage_risk} | {description} | {domain_or_examples} |".format(
                **{k: str(v).replace("|", "/") for k, v in row.items()}
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

