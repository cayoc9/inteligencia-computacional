# Dicionario de Dados: Projeto 2 METABRIC Clinico

Este dicionario cobre o CSV bruto, nomes sanitizados, papeis analiticos, risco de vazamento e features derivadas.

| Raw column | Sanitized column | Raw dtype | Clean dtype | Role | Leakage risk | Description | Domain/examples |
|---|---|---|---|---|---|---|---|
| Patient ID | patient_id | str | string | identifier | none | Coluna original do METABRIC clinico. | MB-0000, MB-0002, MB-0005, MB-0006, MB-0008, MB-0010 |
| Age at Diagnosis | age | float64 | float64 | feature | none | Idade no diagnostico. | 75.65, 43.19, 48.87, 47.68, 76.97, 78.77 |
| Type of Breast Surgery | type_of_breast_surgery | str | string | feature | none | Tipo de cirurgia mamaria registrada. | Mastectomy, Breast Conserving |
| Cancer Type | cancer_type | str | string | feature | none | Coluna original do METABRIC clinico. | Breast Cancer, Breast Sarcoma |
| Cancer Type Detailed | cancer_type_detailed | str | string | feature | none | Coluna original do METABRIC clinico. | Breast Invasive Ductal Carcinoma, Breast Mixed Ductal and Lobular Carcinoma, Breast Invasive Lobular Carcinoma, Invasive Breast Carcinoma, Breast Invasive Mixed Mucinous Carcinoma, Breast Angiosarcoma |
| Cellularity | cellularity | str | string | feature | none | Coluna original do METABRIC clinico. | High, Moderate, Low |
| Chemotherapy | chemotherapy | str | string | feature | none | Indicador de quimioterapia. | No, Yes |
| Pam50 + Claudin-low subtype | pam50_subtype | str | string | feature | none | Subtipo molecular PAM50/Claudin-low. | claudin-low, LumA, LumB, Normal, Her2, Basal |
| Cohort | cohort | float64 | float64 | feature | none | Coluna original do METABRIC clinico. | 1.0, 2.0, 3.0, 5.0, 4.0, 9.0 |
| ER status measured by IHC | er_status_measured_by_ihc | str | string | feature | none | Coluna original do METABRIC clinico. | Positve, Negative |
| ER Status | er_status | str | string | feature | none | Status do receptor de estrogenio. | Positive, Negative |
| Neoplasm Histologic Grade | grade | float64 | float64 | feature | none | Grau histologico tumoral. | 3.0, 2.0, 1.0 |
| HER2 status measured by SNP6 | her2_status_measured_by_snp6 | str | string | feature | none | Coluna original do METABRIC clinico. | Neutral, Loss, Gain, Undef |
| HER2 Status | her2_status | str | string | feature | none | Status HER2. | Negative, Positive |
| Tumor Other Histologic Subtype | tumor_other_histologic_subtype | str | string | feature | none | Coluna original do METABRIC clinico. | Ductal/NST, Mixed, Lobular, Tubular/ cribriform, Mucinous, Medullary |
| Hormone Therapy | hormone_therapy | str | string | feature | none | Indicador de terapia hormonal. | Yes, No |
| Inferred Menopausal State | inferred_menopausal_state | str | string | feature | none | Coluna original do METABRIC clinico. | Post, Pre |
| Integrative Cluster | integrative_cluster | str | string | feature | none | Coluna original do METABRIC clinico. | 4ER+, 3, 9, 7, 4ER-, 5 |
| Primary Tumor Laterality | primary_tumor_laterality | str | string | feature | none | Coluna original do METABRIC clinico. | Right, Left |
| Lymph nodes examined positive | lymph_nodes_positive | float64 | float64 | feature | none | Numero de linfonodos positivos examinados. | 10.0, 0.0, 1.0, 3.0, 8.0, 11.0 |
| Mutation Count | mutation_count | float64 | float64 | feature | none | Contagem de mutacoes reportada. | 2.0, 1.0, 4.0, 5.0, 3.0, 7.0 |
| Nottingham prognostic index | npi | float64 | float64 | feature | none | Indice prognostico de Nottingham. | 6.044, 4.02, 4.03, 4.05, 6.08, 4.062 |
| Oncotree Code | oncotree_code | str | string | feature | none | Coluna original do METABRIC clinico. | IDC, MDLC, ILC, BRCA, IMMC, PBS |
| Overall Survival (Months) | survival_months | float64 | float64 | outcome_time | excluded_primary_model | Coluna original do METABRIC clinico. | 140.5, 84.63333333, 163.7, 164.93333330000002, 41.36666667, 7.8 |
| Overall Survival Status | status | str | int64 | target | none | Coluna original do METABRIC clinico. | Living, Deceased |
| PR Status | pr_status | str | string | feature | none | Status do receptor de progesterona. | Negative, Positive |
| Radio Therapy | radio_therapy | str | string | feature | none | Indicador de radioterapia. | Yes, No |
| Relapse Free Status (Months) | relapse_free_status_months | float64 | float64 | post_outcome_time | excluded_primary_model | Coluna original do METABRIC clinico. | 138.65, 83.52, 151.28, 162.76, 18.55, 2.89 |
| Relapse Free Status | relapse_free_status | str | string | post_outcome_status | excluded_primary_model | Coluna original do METABRIC clinico. | Not Recurred, Recurred |
| Sex | sex | str | string | feature | none | Coluna original do METABRIC clinico. | Female |
| 3-Gene classifier subtype | three_gene_subtype | str | string | feature | none | Coluna original do METABRIC clinico. | ER-/HER2-, ER+/HER2- High Prolif, ER+/HER2- Low Prolif, HER2+ |
| Tumor Size | tumor_size | float64 | float64 | feature | none | Tamanho tumoral. | 22.0, 10.0, 15.0, 25.0, 40.0, 31.0 |
| Tumor Stage | stage | float64 | float64 | feature | none | Estagio tumoral. | 2.0, 1.0, 4.0, 3.0, 0.0 |
| Patient's Vital Status | patient_s_vital_status | str | string | post_outcome_status | excluded_primary_model | Coluna original do METABRIC clinico. | Living, Died of Disease, Died of Other Causes |
|  | node_positive_log1p | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | tumor_grade_burden | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | tumor_stage_burden | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | node_stage_burden | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | nottingham_grade_burden | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | mutation_density | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | large_tumor_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | high_node_burden_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | advanced_stage_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | chemotherapy_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | hormone_therapy_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | radio_therapy_flag | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | treatment_count | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | triple_negative_like | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | hr_positive_her2_negative | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | receptor_profile | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | pam50_risk_group | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | tumor_size_band | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
|  | age_band | derived | derived_after_feature_engineering | derived_feature | none | Feature derivada para capturar risco clinico, molecular ou exposicao a tratamento. |  |
