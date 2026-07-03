# Dicionario de Dados: Projeto 2 Breast Cancer

Este dicionario cobre o CSV bruto, os nomes sanitizados, papeis analiticos, risco de vazamento e features derivadas.

| Raw column | Sanitized column | Raw dtype | Clean dtype | Role | Leakage risk | Description | Domain/examples |
|---|---|---|---|---|---|---|---|
| Age | age | int64 | int64 | feature | none | Patient age at diagnosis | 68, 50, 58, 47, 51, 40 |
| Race | race | str | string | feature | none | Race category | White, Black, Other |
| Marital Status | marital_status | str | string | feature | none | Marital status | Married, Divorced, Single , Widowed, Separated |
| T Stage  | t_stage | str | string | feature | none | Tumor stage category | T1, T2, T3, T4 |
| N Stage | n_stage | str | string | feature | none | Nodal stage category | N1, N2, N3 |
| 6th Stage | 6th_stage | str | string | feature | none | AJCC 6th stage grouping | IIA, IIIA, IIIC, IIB, IIIB |
| differentiate | differentiate | str | string | feature | none | Tumor differentiation | Poorly differentiated, Moderately differentiated, Well differentiated, Undifferentiated |
| Grade | grade | str | int64 | feature | none | Tumor grade, ordinal 1-4 after sanitation | 3, 2, 1,  anaplastic; Grade IV |
| A Stage | a_stage | str | string | feature | none | Regional or distant stage | Regional, Distant |
| Tumor Size | tumor_size | int64 | int64 | feature | none | Tumor size | 4, 35, 63, 18, 41, 20 |
| Estrogen Status | estrogen_status | str | string | feature | none | Estrogen receptor status | Positive, Negative |
| Progesterone Status | progesterone_status | str | string | feature | none | Progesterone receptor status | Positive, Negative |
| Regional Node Examined | regional_node_examined | int64 | int64 | feature | none | Number of regional nodes examined | 24, 14, 2, 3, 18, 11 |
| Reginol Node Positive | regional_node_positive | int64 | int64 | feature | none | Number of positive regional nodes | 1, 5, 7, 2, 18, 12 |
| Survival Months | survival_months | int64 | int64 | excluded_primary_model | leakage/follow_up_risk | Follow-up survival time in months | 60, 62, 75, 84, 50, 89 |
| Status | status | str | int64 | target | none | Survival status: Alive=0, Dead=1 | Alive, Dead |
|  | node_positive_ratio | derived | float64 | derived_feature | none | regional_node_positive / regional_node_examined, clipped to 0-1 | 0.0-1.0 |
|  | advanced_stage_flag | derived | int64 | derived_feature | none | 1 when 6th_stage is IIIB or IIIC, else 0 | 0, 1 |
|  | hormone_receptor_negative | derived | int64 | derived_feature | none | 1 when estrogen or progesterone status is Negative | 0, 1 |
|  | tumor_node_burden | derived | float64 | derived_feature | none | tumor_size * (1 + node_positive_ratio) | positive numeric |
