#!/usr/bin/env python3
"""Adiciona a Seção 9 (Diagnóstico) ao notebook principal."""

import json
from pathlib import Path
import nbformat as nbf

PROJECT_ROOT = Path.cwd()
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "trabalho_1_classificacao_saude_rf_vs_rn.ipynb"

nb = nbf.read(NOTEBOOK_PATH, as_version=4)

# ─── Seção 9 ─────────────────────────────────────────────────────────────────

cells = []

# 9.0 - Título
cells.append(nbf.v4.new_markdown_cell(
    "## 9. Diagnostico Avancado e Analise de Threshold\n\n"
    "Esta secao incorpora os resultados da Rodada 3 (Diagnostico), "
    "estendendo a analise comparativa com:\n\n"
    "- **Comparacao ampliada:** 5 modelos (incluindo HistGradientBoosting e Logistic Regression)\n"
    "- **Threshold tuning:** Otimizacao do ponto de corte para maximizar F1 e Balanced Accuracy\n"
    "- **Feature importance:** Permutation importance para identificar features dominantes\n"
    "- **Analise de ambiguidade:** Por que o teto de performance e de ~74%\n"
    "- **Recomendacao de threshold para producao:** Contexto de saude ocupacional (risco de Burnout)\n\n"
    "Os dados foram gerados pelo script `scripts/diagnose_model_limits.py` "
    "e estao disponiveis em `reports/diagnostics/`."
))

# 9.1 - Carga dos dados
cells.append(nbf.v4.new_code_cell(
    "import pandas as pd\n"
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "import seaborn as sns\n"
    "from pathlib import Path\n"
    "import json\n\n"
    "DIAG_DIR = Path.cwd() / 'reports' / 'diagnostics'\n"
    "FIGURES_DIR = Path.cwd() / 'reports' / 'figures'\n\n"
    "with open(DIAG_DIR / 'diagnostics_summary.json') as f:\n"
    "    summary = json.load(f)\n\n"
    "holdout = pd.read_csv(DIAG_DIR / 'holdout_model_comparison.csv')\n"
    "threshold_df = pd.read_csv(DIAG_DIR / 'threshold_scan_best_model.csv')\n"
    "importance = pd.read_csv(DIAG_DIR / 'permutation_importance_best_model.csv')\n\n"
    "print('Diagnostico carregado com sucesso!')\n"
    "print(f'Modelos comparados: {len(holdout)}')\n"
    "print(f'Thresholds analisados: {len(threshold_df)}')\n"
    "print(f'Features avaliadas: {len(importance)}')\n\n"
    "baseline = summary['majority_baseline']\n"
    "print(f'\\nBaseline (classe majoritaria): accuracy={baseline[\"accuracy\"]:.4f}',\n"
    "      f'F1={baseline[\"f1\"]}, ROC AUC={baseline[\"roc_auc\"]}')"
))

# 9.2 - Comparação ampliada
cells.append(nbf.v4.new_markdown_cell(
    "### 9.1 Comparacao Ampliada de Modelos\n\n"
    "A tabela abaixo inclui modelos adicionais testados no diagnostico "
    "(HistGradientBoosting, Logistic Regression, Extra Trees) "
    "alem da RF e RN do pipeline principal."
))

cells.append(nbf.v4.new_code_cell(
    "display_cols = ['modelo', 'accuracy', 'balanced_accuracy', 'precision', 'recall', 'f1', 'roc_auc']\n"
    "display_names = {\n"
    "    'modelo': 'Modelo', 'accuracy': 'Acuracia',\n"
    "    'balanced_accuracy': 'Balanced Acc', 'precision': 'Precisao',\n"
    "    'recall': 'Recall', 'f1': 'F1', 'roc_auc': 'ROC AUC'\n"
    "}\n\n"
    "comparison_display = holdout[display_cols].rename(columns=display_names).copy()\n"
    "comparison_display = comparison_display.round(4)\n"
    "display(comparison_display.style.bar(subset=['ROC AUC'], color='#2166AC'))\n\n"
    "print('Melhor modelo geral: HistGradientBoosting (74,25% accuracy, 82,58% ROC AUC)')\n"
    "print('Diferenca para RF: apenas 0,1 pp - empate tecnico')\n"
    "print('Todos os modelos convergem para ~74% - teto do alvo, nao do modelo')"
))

# 9.3 - Threshold tuning
cells.append(nbf.v4.new_markdown_cell(
    "### 9.2 Otimizacao de Threshold\n\n"
    "O threshold padrao de 0,5 nao e ideal para este dataset desbalanceado (61%/39%). "
    "Ajustar o ponto de corte pode melhorar o F1-Score sem retreinar o modelo."
))

cells.append(nbf.v4.new_code_cell(
    "best_f1_idx = threshold_df['f1'].idxmax()\n"
    "best_bal_idx = threshold_df['balanced_accuracy'].idxmax()\n"
    "std_idx = threshold_df[threshold_df['threshold'] == 0.5].index[0]\n\n"
    "best_f1_row = threshold_df.loc[best_f1_idx]\n"
    "best_bal_row = threshold_df.loc[best_bal_idx]\n"
    "std_row = threshold_df.loc[std_idx]\n\n"
    "print('=== Threshold Padrao vs Otimizado ===')\n"
    "print(f\"{'':20s} {'Padrao (0.50)':>15s} {'F1 otimo':>15s} {'BalAcc otimo':>15s}\")\n"
    "print(f\"{'─'*65}\")\n"
    "print(f\"{'Threshold':20s} {std_row['threshold']:>15.2f} {best_f1_row['threshold']:>15.2f} {best_bal_row['threshold']:>15.2f}\")\n"
    "print(f\"{'Acuracia':20s} {std_row['accuracy']:>15.4f} {best_f1_row['accuracy']:>15.4f} {best_bal_row['accuracy']:>15.4f}\")\n"
    "print(f\"{'F1-Score':20s} {std_row['f1']:>15.4f} {best_f1_row['f1']:>15.4f} {best_bal_row['f1']:>15.4f}\")\n\n"
    "gain = (best_f1_row['f1'] - std_row['f1']) / std_row['f1'] * 100\n"
    "print(f'\\nGanho no F1 com threshold {best_f1_row[\"threshold\"]:.2f}: {gain:.1f}%')\n\n"
    "plt.figure(figsize=(12, 6))\n"
    "plt.plot(threshold_df['threshold'], threshold_df['f1'], 'b-', lw=2.5, label='F1-Score')\n"
    "plt.plot(threshold_df['threshold'], threshold_df['recall'], 'r--', lw=1.5, label='Recall')\n"
    "plt.plot(threshold_df['threshold'], threshold_df['precision'], 'g--', lw=1.5, label='Precisao')\n"
    "plt.axvline(x=0.5, color='gray', linestyle=':', alpha=0.7)\n"
    "plt.axvline(x=best_f1_row['threshold'], color='green', linestyle='--', alpha=0.8)\n"
    "plt.xlabel('Threshold de Decisao')\n"
    "plt.ylabel('Score')\n"
    "plt.title('Otimizacao de Threshold - Ganho de 6% no F1-Score')\n"
    "plt.legend(loc='lower left')\n"
    "plt.xlim(0.15, 0.75)\n"
    "plt.grid(True, alpha=0.3)\n"
    "plt.tight_layout()\n"
    "plt.show()"
))

# 9.4 - Contexto saúde
cells.append(nbf.v4.new_markdown_cell(
    "### 9.3 Impacto no Contexto de Saude Ocupacional\n\n"
    "Em aplicacoes de saude, a escolha do threshold tem consequencias diretas:\n\n"
    "- **Falso Positivo (FP):** Pessoa classificada como descansada quando nao esta -> risco ocupacional (Burnout)\n"
    "- **Falso Negativo (FN):** Pessoa classificada como nao descansada quando esta -> oportunidade perdida\n\n"
    "Para o contexto de saude do sono, **minimizar Falsos Positivos** deve ser priorizado, "
    "pois mascarar fadiga acumulada pode ter consequencias mais graves. "
    "Portanto, thresholds mais altos sao preferiveis em producao, mesmo que reduzam o F1."
))

# 9.5 - Feature importance
cells.append(nbf.v4.new_markdown_cell(
    "### 9.4 Importancia de Features\n\n"
    "A analise de Permutation Importance (quebra do AUC ao permutar cada feature) "
    "revela quais variaveis realmente carregam o sinal preditivo."
))

cells.append(nbf.v4.new_code_cell(
    "top_n = 10\n"
    "top_features = importance.head(top_n).copy()\n\n"
    "feature_labels = {\n"
    "    'sleep_duration_hrs': 'Duracao do sono (hrs)',\n"
    "    'sleep_quality_score': 'Qualidade do sono',\n"
    "    'wake_episodes_per_night': 'Episodios de acordar',\n"
    "    'stress_score': 'Nivel de estresse',\n"
    "}\n\n"
    "top_features['feature_label'] = top_features['feature'].map(feature_labels).fillna(top_features['feature'])\n"
    "total_imp = top_features['importance_mean_auc_drop'].sum()\n"
    "top_features['pct'] = top_features['importance_mean_auc_drop'] / total_imp * 100\n"
    "top_4_pct = top_features.head(4)['pct'].sum()\n\n"
    "print('=== Top 10 Features por Permutation Importance ===')\n"
    "print(top_features[['feature_label', 'importance_mean_auc_drop', 'pct']].to_string(index=False))\n"
    "print(f'\\nApenas 4 features concentram {top_4_pct:.0f}% do poder preditivo.')\n\n"
    "fig, ax = plt.subplots(figsize=(12, 7))\n"
    "plot_data = top_features.sort_values('importance_mean_auc_drop', ascending=True)\n"
    "colors = ['#2166AC'] * 4 + ['#B3B3B3'] * (len(plot_data) - 4)\n"
    "bars = ax.barh(range(len(plot_data)), plot_data['importance_mean_auc_drop'], color=colors, height=0.6)\n"
    "ax.set_yticks(range(len(plot_data)))\n"
    "ax.set_yticklabels(plot_data['feature_label'], fontsize=10)\n"
    "ax.set_xlabel('Queda no AUC ao permutar a feature', fontsize=11)\n"
    "ax.set_title('Importancia de Features - Permutation Importance (HistGB)', fontsize=14, fontweight='bold')\n"
    "for i, (bar, val) in enumerate(zip(bars, plot_data['importance_mean_auc_drop'])):\n"
    "    ax.text(bar.get_width() + 0.001, bar.get_y() + bar.get_height()/2, f'{val:.4f}', va='center', fontsize=9)\n"
    "ax.axhline(y=3.5, color='#D3D3D3', linestyle='--', linewidth=1)\n"
    "plt.tight_layout()\n"
    "plt.show()"
))

# 9.6 - Ambiguidade
cells.append(nbf.v4.new_markdown_cell(
    "### 9.5 Analise de Ambiguidade do Alvo\n\n"
    "Por que todos os modelos convergem para ~74% e nao vao alem?\n\n"
    "O diagnostico de ambiguidade agrupou registros com perfis similares "
    "e verificou se o target variava dentro do mesmo grupo."
))

cells.append(nbf.v4.new_code_cell(
    "amb = summary['ambiguity_summary']\n"
    "print('=== Diagnostico de Ambiguidade do Target ===')\n"
    "print(f'Grupos analisados: {amb[\"groups_count\"]}')\n"
    "print(f'Taxa media de minoria intra-grupo: {amb[\"mean_minority_rate\"]:.2%}')\n"
    "print(f'Percentil 75: {amb[\"p75_minority_rate\"]:.2%}')\n"
    "print(f'Percentil 90: {amb[\"p90_minority_rate\"]:.2%}')\n\n"
    "print('\\nInterpretacao:')\n"
    "print('Dentro de grupos com perfil de sono semelhante, ate 33% (P75) das')\n"
    "print('pessoas respondem de forma DIFERENTE sobre se estao descansadas.')\n"
    "print('O target tem ruido intrinseco - a percepcao subjetiva de')\n"
    "print('descanso varia entre individuos mesmo com condicoes objetivas similares.')\n\n"
    "print('Causas provaveis:')\n"
    "print('1. Subjetividade: pergunta subjetiva')\n"
    "print('2. Features ausentes: dieta, genetica, condicoes psicologicas')\n"
    "print('3. Target composto: felt_rested + cognitive_performance_score')"
))

# 9.7 - Feature AUC individual
cells.append(nbf.v4.new_markdown_cell(
    "### 9.6 Poder Preditivo Individual (AUC por Feature)\n\n"
    "Qual o poder de cada feature isolada para prever felt_rested?"
))

cells.append(nbf.v4.new_code_cell(
    "top_single = summary['top_numeric_single_feature_auc'][:8]\n"
    "single_df = pd.DataFrame(top_single)\n"
    "single_df['feature_label'] = single_df['feature'].map({\n"
    "    'sleep_quality_score': 'Qualidade do sono',\n"
    "    'sleep_duration_hrs': 'Duracao do sono',\n"
    "    'cognitive_performance_score': 'Performance cognitiva*',\n"
    "    'stress_score': 'Estresse (invertido)',\n"
    "    'work_hours_that_day': 'Horas de trabalho',\n"
    "    'wake_episodes_per_night': 'Episodios de acordar',\n"
    "    'sleep_latency_mins': 'Latencia do sono',\n"
    "    'rem_percentage': '% REM',\n"
    "}).fillna(single_df['feature'])\n\n"
    "display(single_df[['feature_label', 'auc_direction_adjusted']].style\n"
    "    .format({'auc_direction_adjusted': '{:.4f}'})\n"
    "    .bar(subset=['auc_direction_adjusted'], color='#2166AC'))\n\n"
    "print()\n"
    "print('* cognitive_performance_score foi REMOVIDA do treino (vazamento conceitual)')\n"
    "print('  Seu alto AUC (0.771) sugere que um target composto (V2) pode ser interessante')"
))

# 9.8 - Síntese
cells.append(nbf.v4.new_markdown_cell(
    "### 9.7 Sintese do Diagnostico\n\n"
    "**Descobertas principais:**\n\n"
    "1. **Teto de 74%:** Todos os modelos convergem para o mesmo patamar. "
    "O gargalo e o alvo subjetivo, nao o algoritmo.\n\n"
    "2. **Threshold importa:** Ajustar de 0,50 para 0,35 melhora o F1 em 6,1% "
    "sem retreinar. A escolha deve considerar o contexto.\n\n"
    "3. **4 features dominam:** Duracao do sono, qualidade do sono, "
    "estresse e episodios de acordar concentram ~80% do sinal.\n\n"
    "4. **Feature engineering nao rompeu o teto:** Features derivadas "
    "nao superaram o limite de 74%.\n\n"
    "5. **Target composto (V2):** Combinar felt_rested com "
    "cognitive_performance_score pode gerar um target mais objetivo.\n\n"
    "**Recomendacao final:** Para classificacao em dados tabulares de saude, "
    "comece com Random Forest ou Gradient Boosting. Reserve Redes Neurais "
    "para problemas com grandes volumes de dados nao-estruturados."
))

# ─── Inserir células no notebook ─────────────────────────────────────────────

for cell in cells:
    nb.cells.append(cell)

nbf.write(nb, NOTEBOOK_PATH)

print(f"Secao 9 adicionada ao notebook!")
print(f"{len(cells)} novas celulas inseridas")
print(f"Total de celulas: {len(nb.cells)}")
