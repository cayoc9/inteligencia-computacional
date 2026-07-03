from __future__ import annotations

import pandas as pd

from breast_cancer_survival.data import clean_column_name


LEAKAGE_COLUMNS = {
    "Overall Survival (Months)": "outcome_time",
    "Overall Survival Status": "target",
    "Relapse Free Status (Months)": "post_outcome_time",
    "Relapse Free Status": "post_outcome_status",
    "Patient's Vital Status": "post_outcome_status",
}


DESCRIPTION_OVERRIDES = {
    "Age at Diagnosis": "Idade no diagnostico.",
    "Type of Breast Surgery": "Tipo de cirurgia mamaria registrada.",
    "Chemotherapy": "Indicador de quimioterapia.",
    "Hormone Therapy": "Indicador de terapia hormonal.",
    "Radio Therapy": "Indicador de radioterapia.",
    "Pam50 + Claudin-low subtype": "Subtipo molecular PAM50/Claudin-low.",
    "ER Status": "Status do receptor de estrogenio.",
    "PR Status": "Status do receptor de progesterona.",
    "HER2 Status": "Status HER2.",
    "Neoplasm Histologic Grade": "Grau histologico tumoral.",
    "Lymph nodes examined positive": "Numero de linfonodos positivos examinados.",
    "Mutation Count": "Contagem de mutacoes reportada.",
    "Nottingham prognostic index": "Indice prognostico de Nottingham.",
    "Tumor Size": "Tamanho tumoral.",
    "Tumor Stage": "Estagio tumoral.",
}


DERIVED_FEATURES = [
    "node_positive_log1p",
    "tumor_grade_burden",
    "tumor_stage_burden",
    "node_stage_burden",
    "nottingham_grade_burden",
    "mutation_density",
    "large_tumor_flag",
    "high_node_burden_flag",
    "advanced_stage_flag",
    "chemotherapy_flag",
    "hormone_therapy_flag",
    "radio_therapy_flag",
    "treatment_count",
    "triple_negative_like",
    "hr_positive_her2_negative",
    "receptor_profile",
    "pam50_risk_group",
    "tumor_size_band",
    "age_band",
]


def _examples(series: pd.Series, limit: int = 6) -> str:
    values = series.dropna().astype(str).drop_duplicates().head(limit).tolist()
    return ", ".join(values)


def _role_for(raw_col: str) -> str:
    if raw_col in LEAKAGE_COLUMNS:
        return LEAKAGE_COLUMNS[raw_col]
    if raw_col == "Patient ID":
        return "identifier"
    return "feature"


def _leakage_for(raw_col: str) -> str:
    if raw_col in {"Overall Survival (Months)", "Relapse Free Status (Months)", "Relapse Free Status", "Patient's Vital Status"}:
        return "excluded_primary_model"
    return "none"


def build_data_dictionary(raw: pd.DataFrame, clean: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for raw_col in raw.columns:
        sanitized_col = clean_column_name(raw_col)
        sanitized_col = {
            "overall_survival_months": "survival_months",
            "overall_survival_status": "status",
            "age_at_diagnosis": "age",
            "neoplasm_histologic_grade": "grade",
            "lymph_nodes_examined_positive": "lymph_nodes_positive",
            "pam50_plus_claudin_low_subtype": "pam50_subtype",
            "3_gene_classifier_subtype": "three_gene_subtype",
            "nottingham_prognostic_index": "npi",
            "tumor_stage": "stage",
        }.get(sanitized_col, sanitized_col)
        rows.append(
            {
                "raw_column": raw_col,
                "sanitized_column": sanitized_col,
                "raw_dtype": str(raw[raw_col].dtype),
                "clean_dtype": str(clean[sanitized_col].dtype) if sanitized_col in clean.columns else "dropped_or_renamed",
                "role": _role_for(raw_col),
                "leakage_risk": _leakage_for(raw_col),
                "description": DESCRIPTION_OVERRIDES.get(raw_col, "Coluna original do METABRIC clinico."),
                "domain_or_examples": _examples(raw[raw_col]),
            }
        )
    for feature in DERIVED_FEATURES:
        rows.append(
            {
                "raw_column": "",
                "sanitized_column": feature,
                "raw_dtype": "derived",
                "clean_dtype": str(clean[feature].dtype) if feature in clean.columns else "derived_after_feature_engineering",
                "role": "derived_feature",
                "leakage_risk": "none",
                "description": "Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento.",
                "domain_or_examples": "",
            }
        )
    return pd.DataFrame(rows)


def write_data_dictionary(dictionary: pd.DataFrame, path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Dicionario de Dados: Projeto 2 METABRIC Clinico",
        "",
        "Este dicionario cobre o CSV bruto, nomes sanitizados, papeis analiticos, risco de vazamento e features derivadas.",
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
