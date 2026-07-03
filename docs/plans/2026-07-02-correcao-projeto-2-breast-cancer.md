# Correcao Projeto 2 Breast Cancer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

> **TLC Spec-Driven Canonical Source:** este arquivo agora e um plano de apoio. A fonte canonica para requisitos, desenho e execucao e `.specs/features/trabalho-2-breast-cancer/`:
>
> - `spec.md`: WHAT, requisitos rastreaveis e criterios de aceite.
> - `design.md`: HOW, arquitetura, componentes e artefatos.
> - `tasks.md`: tarefas atomicas, dependencias, gates e traceabilidade.
>
> Antes de executar qualquer tarefa, leia os tres arquivos acima. Se houver conflito, os artefatos `.specs/features/trabalho-2-breast-cancer/` vencem este plano.

**Goal:** Corrigir o Projeto 2 para que o dataset SEER Breast Cancer seja analisado, saneado, modelado e apresentado com objetivo clinico claro, sem vazamento de alvo, com EDA rastreavel, engenharia de features defensavel, metricas orientadas a falso negativo e ensemble ponderado.

**Architecture:** Separar o projeto em um pacote pequeno de funcoes reutilizaveis (`src/breast_cancer_survival/`) e scripts auditaveis na raiz do `projeto_2_neuro_fuzzy/`. O fluxo deve ser: contrato dos dados -> sanitizacao -> EDA -> features -> treino comparativo -> threshold/ensemble -> comparativo neuro-fuzzy -> relatorios. O modelo principal deve responder ao objetivo "prever risco de obito a partir de atributos clinicos disponiveis no diagnostico", portanto `Survival Months` deve sair do conjunto principal de features e aparecer apenas em analise de sensibilidade sobre vazamento/follow-up.

**Tech Stack:** Python 3.12, pandas, numpy, scikit-learn, matplotlib, seaborn, joblib, pytest. XGBoost e imbalanced-learn ficam opcionais; o plano base deve funcionar apenas com as dependencias ja aceitas em `requirements.txt` mais `pytest`.

---

## Contexto e Diagnostico Atual

O projeto atual em `projeto_2_neuro_fuzzy/` tem apenas:

- `baseline.py`: treina Random Forest e MLP sobre todas as colunas exceto `Status`.
- `hybrid_neuro_fuzzy.py`: fuzzifica manualmente `Age`, `Tumor Size` e `Reginol Node Positive`, concatena categoricas e treina MLP.
- `analise_audio_estrategia.md`: documenta que o audio recomenda EDA, modelos tabulares, ensemble ponderado, cuidado com overfit e foco em precision/recall/falsos negativos.
- `dataset/Breast_Cancer.csv`: 4024 linhas, 16 colunas.

Problemas encontrados:

- O baseline usa `Survival Months` como feature, embora o alvo seja `Status`. Para predicao clinica em diagnostico, isso e vazamento conceitual porque meses de sobrevida sao informacao posterior ao desfecho.
- Nao existe EDA especifica versionada para o projeto 2.
- Nao existe sanitizacao centralizada de nomes e valores.
- Existem problemas de schema: `T Stage ` tem espaco final, `Reginol Node Positive` tem erro de grafia, `Marital Status` contem `Single ` com espaco, `Grade` mistura numeros como texto e ` anaplastic; Grade IV`.
- Ha 1 linha duplicada.
- O alvo e desbalanceado: `Alive = 3408` e `Dead = 616` (`Dead = 15,31%`).
- O neuro-fuzzy atual nao e ANFIS completo; e um modelo cooperativo com fuzzificacao manual + MLP.
- O modelo neuro-fuzzy atual piora o criterio clinico principal: 94 falsos negativos contra 63 do Random Forest atual.
- A selecao de modelo ainda nao otimiza explicitamente recall, F2, PR AUC ou falso negativo.
- Nao ha ensemble implementado.
- Nao ha notebook Jupyter especifico do Projeto 2, apesar da convencao do repositorio de manter um notebook narrativo por projeto.
- Nao ha dicionario de dados do Projeto 2 com nomes brutos/sanitizados, dominio, papel analitico, risco de vazamento e features derivadas.
- Nao ha analise de metadados e relacoes dentro da EDA, embora isso devesse orientar a escolha dos modelos e a politica de vazamento.

## Criterios de Aceite

- `pytest -q` passa.
- `python projeto_2_neuro_fuzzy/01_validate_data.py` gera relatorio de contrato dos dados.
- `python projeto_2_neuro_fuzzy/02_eda.py` gera figuras e resumo em `projeto_2_neuro_fuzzy/reports/`.
- `projeto_2_neuro_fuzzy/docs/DATA_DICTIONARY.md` existe e cobre colunas brutas, colunas sanitizadas, papeis analiticos, risco de vazamento e features derivadas.
- `projeto_2_neuro_fuzzy/reports/tables/metadata_profile.csv` existe e documenta dtype, nulos, cardinalidade, exemplos, papel analitico e flag de vazamento.
- `projeto_2_neuro_fuzzy/reports/tables/numeric_relationships.csv` e `categorical_relationships.csv` existem como parte da EDA.
- `python projeto_2_neuro_fuzzy/03_train_models.py` compara no minimo Logistic Regression, Random Forest, ExtraTrees, HistGradientBoosting, SVM calibrado e MLP.
- `python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py` gera threshold scan, ensemble soft voting ponderado e tabela final com falsos negativos.
- `python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py` roda o neuro-fuzzy como comparativo academico, com a mesma sanitizacao, split e metricas do pipeline principal.
- `projeto_2_neuro_fuzzy/notebooks/projeto_2_breast_cancer_survival.ipynb` existe e executa com `jupyter nbconvert --execute`.
- Resultado principal nao usa `Survival Months` como feature.
- Relatorio final explicita qual objetivo foi testado antes e qual objetivo corrigido passa a ser testado.
- Documentacao em `.specs/`, `STATUS.md` e `projeto_2_neuro_fuzzy/README.md` reflete o novo estado.

---

### Task 1: Criar Spec Canonica do Trabalho 2

**Files:**
- Create: `.specs/features/trabalho-2-breast-cancer/spec.md`
- Create: `.specs/features/trabalho-2-breast-cancer/tasks.md`
- Modify: `.specs/project/ROADMAP.md`
- Modify: `.specs/project/STATE.md`
- Modify: `STATUS.md`

**Step 1: Write the failing documentation check**

Create `tests/test_project2_docs.py`:

```python
from pathlib import Path


def test_trabalho_2_spec_exists_and_defines_objective():
    spec = Path(".specs/features/trabalho-2-breast-cancer/spec.md")
    assert spec.exists()
    text = spec.read_text(encoding="utf-8")
    assert "Objetivo corrigido" in text
    assert "Survival Months" in text
    assert "falsos negativos" in text
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest tests/test_project2_docs.py::test_trabalho_2_spec_exists_and_defines_objective -q
```

Expected: FAIL because `tests/` and the spec do not exist.

**Step 3: Write minimal docs**

Create `.specs/features/trabalho-2-breast-cancer/spec.md`:

```markdown
# Trabalho 2: Breast Cancer Survival Risk

## Objetivo Corrigido

Prever risco de obito (`Status = Dead`) a partir de atributos clinicos disponiveis no diagnostico.

## Objetivo Testado Antes

O baseline anterior predizia `Status` usando todas as colunas exceto o alvo, incluindo `Survival Months`. Isso responde a uma pergunta contaminada por informacao posterior ao acompanhamento, nao a uma predicao clinica em diagnostico.

## Politica de Vazamento

- `Status` e o alvo.
- `Survival Months` nao entra no modelo principal.
- `Survival Months` pode aparecer apenas em analise de sensibilidade para mostrar o impacto do vazamento/follow-up.

## Metrica Principal

Priorizar reducao de falsos negativos para `Dead`, acompanhada por recall, precision, F2, PR AUC e matriz de confusao.

## Estrategia

1. Sanitizar dados.
2. Fazer EDA.
3. Criar features clinicas defensaveis.
4. Testar modelos tabulares.
5. Ajustar threshold.
6. Montar ensemble ponderado.
7. Comparar neuro-fuzzy como abordagem academica.
```

Create `.specs/features/trabalho-2-breast-cancer/tasks.md`:

```markdown
# Tasks: Trabalho 2 Breast Cancer

- [ ] T2-01: Contrato e sanitizacao dos dados
- [ ] T2-02: EDA especifica
- [ ] T2-03: Engenharia de features clinicas
- [ ] T2-04: Suite de modelos tabulares
- [ ] T2-05: Threshold tuning orientado a falso negativo
- [ ] T2-06: Ensemble ponderado
- [ ] T2-07: Comparativo neuro-fuzzy
- [ ] T2-08: Relatorio e apresentacao
```

Update `.specs/project/ROADMAP.md`, `.specs/project/STATE.md` and `STATUS.md` to mark Trabalho 2 as "Em correcao metodologica".

**Step 4: Run test to verify it passes**

Run:

```bash
pytest tests/test_project2_docs.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add tests/test_project2_docs.py .specs/features/trabalho-2-breast-cancer .specs/project/ROADMAP.md .specs/project/STATE.md STATUS.md
git commit -m "docs: define corrected scope for breast cancer project"
```

---

### Task 2: Criar Estrutura de Pacote e Test Harness

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/__init__.py`
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/config.py`
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/paths.py`
- Create: `projeto_2_neuro_fuzzy/tests/conftest.py`
- Modify: `requirements.txt`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_paths.py`:

```python
from pathlib import Path

from breast_cancer_survival.paths import DATASET_PATH, REPORTS_DIR


def test_project_paths_resolve_inside_project():
    assert DATASET_PATH.name == "Breast_Cancer.csv"
    assert DATASET_PATH.exists()
    assert REPORTS_DIR == Path("projeto_2_neuro_fuzzy/reports")
```

Create `projeto_2_neuro_fuzzy/tests/conftest.py`:

```python
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "projeto_2_neuro_fuzzy" / "src"
sys.path.insert(0, str(SRC))
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_paths.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'breast_cancer_survival'`.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/paths.py`:

```python
from pathlib import Path

PROJECT_DIR = Path("projeto_2_neuro_fuzzy")
DATASET_PATH = PROJECT_DIR / "dataset" / "Breast_Cancer.csv"
REPORTS_DIR = PROJECT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"
MODELS_DIR = PROJECT_DIR / "models"
```

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/config.py`:

```python
RANDOM_STATE = 42
TEST_SIZE = 0.2
POSITIVE_LABEL = 1
NEGATIVE_LABEL = 0
TARGET_COLUMN = "status"
LEAKAGE_COLUMNS = ["survival_months"]
```

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/__init__.py`:

```python
"""Utilities for the Projeto 2 breast cancer survival-risk pipeline."""
```

Add `pytest>=8.0.0,<9.0.0` to `requirements.txt`.

**Step 4: Run test to verify it passes**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_paths.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add requirements.txt projeto_2_neuro_fuzzy/src projeto_2_neuro_fuzzy/tests
git commit -m "test: add project 2 package harness"
```

---

### Task 3: Implementar Contrato e Sanitizacao dos Dados

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/data.py`
- Create: `projeto_2_neuro_fuzzy/01_validate_data.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_data_sanitization.py`

**Step 1: Write the failing tests**

Create `projeto_2_neuro_fuzzy/tests/test_data_sanitization.py`:

```python
import pandas as pd

from breast_cancer_survival.data import clean_column_name, load_raw_data, sanitize_data


def test_clean_column_name_normalizes_known_issues():
    assert clean_column_name("T Stage ") == "t_stage"
    assert clean_column_name("Reginol Node Positive") == "regional_node_positive"
    assert clean_column_name("Survival Months") == "survival_months"


def test_sanitize_data_trims_values_maps_target_and_removes_duplicate():
    raw = load_raw_data()
    cleaned = sanitize_data(raw)

    assert "t_stage" in cleaned.columns
    assert "reginol_node_positive" not in cleaned.columns
    assert "regional_node_positive" in cleaned.columns
    assert cleaned["marital_status"].str.endswith(" ").sum() == 0
    assert set(cleaned["status"].unique()) == {0, 1}
    assert cleaned.duplicated().sum() == 0
    assert len(cleaned) == len(raw.drop_duplicates())


def test_grade_is_numeric_ordered_after_sanitization():
    cleaned = sanitize_data(load_raw_data())
    assert pd.api.types.is_integer_dtype(cleaned["grade"])
    assert set(cleaned["grade"].unique()) <= {1, 2, 3, 4}
```

**Step 2: Run tests to verify they fail**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_data_sanitization.py -q
```

Expected: FAIL because `data.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/data.py`:

```python
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
    cleaned = CANONICAL_RENAMES.get(cleaned, cleaned)
    return cleaned


def load_raw_data(path: Path = DATASET_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def sanitize_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = [clean_column_name(col) for col in cleaned.columns]

    text_cols = cleaned.select_dtypes(include=["object", "string"]).columns
    for col in text_cols:
        cleaned[col] = cleaned[col].astype("string").str.strip()

    cleaned["status"] = cleaned["status"].map(TARGET_MAP).astype("int64")
    cleaned["grade"] = (
        cleaned["grade"]
        .astype("string")
        .str.strip()
        .str.lower()
        .map(GRADE_MAP)
        .astype("int64")
    )

    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    return cleaned
```

Create `projeto_2_neuro_fuzzy/01_validate_data.py`:

```python
from breast_cancer_survival.data import load_raw_data, sanitize_data


def main():
    raw = load_raw_data()
    cleaned = sanitize_data(raw)
    print("Raw shape:", raw.shape)
    print("Clean shape:", cleaned.shape)
    print("Missing values:", int(cleaned.isna().sum().sum()))
    print("Duplicates:", int(cleaned.duplicated().sum()))
    print("Target counts:")
    print(cleaned["status"].value_counts().sort_index())


if __name__ == "__main__":
    main()
```

**Step 4: Run tests and validation**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_data_sanitization.py -q
python projeto_2_neuro_fuzzy/01_validate_data.py
```

Expected: tests PASS; validation prints 4023 cleaned rows, 0 missing values, 0 duplicates.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/data.py projeto_2_neuro_fuzzy/01_validate_data.py projeto_2_neuro_fuzzy/tests/test_data_sanitization.py
git commit -m "feat: sanitize breast cancer dataset"
```

---

### Task 4: Formalizar Objetivo, Feature Set e Politica de Vazamento

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_feature_policy.py`
- Modify: `projeto_2_neuro_fuzzy/analise_audio_estrategia.md`

**Step 1: Write the failing tests**

Create `projeto_2_neuro_fuzzy/tests/test_feature_policy.py`:

```python
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import split_features_target


def test_main_feature_set_excludes_target_and_survival_months():
    df = sanitize_data(load_raw_data())
    X, y = split_features_target(df, include_survival_months=False)

    assert "status" not in X.columns
    assert "survival_months" not in X.columns
    assert y.name == "status"
    assert set(y.unique()) == {0, 1}


def test_leakage_sensitivity_can_include_survival_months_explicitly():
    df = sanitize_data(load_raw_data())
    X, _ = split_features_target(df, include_survival_months=True)

    assert "survival_months" in X.columns
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_feature_policy.py -q
```

Expected: FAIL because `features.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py`:

```python
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
```

Append to `projeto_2_neuro_fuzzy/analise_audio_estrategia.md`:

```markdown
## Revisao do objetivo testado

O baseline anterior testava `Status` usando `Survival Months` como feature. Para uma pergunta clinica de predicao em diagnostico, isso introduz vazamento conceitual. O objetivo corrigido passa a excluir `Survival Months` do modelo principal e usa essa coluna apenas em analise de sensibilidade.
```

**Step 4: Run test to verify it passes**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_feature_policy.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py projeto_2_neuro_fuzzy/tests/test_feature_policy.py projeto_2_neuro_fuzzy/analise_audio_estrategia.md
git commit -m "fix: exclude survival months from primary objective"
```

---

### Task 5: Implementar EDA Especifica e Persistente

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/eda.py`
- Create: `projeto_2_neuro_fuzzy/02_eda.py`
- Create: `projeto_2_neuro_fuzzy/reports/README.md`
- Test: `projeto_2_neuro_fuzzy/tests/test_eda_outputs.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_eda_outputs.py`:

```python
from pathlib import Path

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.eda import build_eda_summary


def test_build_eda_summary_contains_target_and_leakage_signal():
    df = sanitize_data(load_raw_data())
    summary = build_eda_summary(df)

    assert summary["rows"] == 4023
    assert summary["target_counts"][1] == 616
    assert "survival_months" in summary["numeric_correlations_with_dead"]
    assert summary["numeric_correlations_with_dead"]["survival_months"] < -0.4
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_eda_outputs.py -q
```

Expected: FAIL because `eda.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/eda.py`:

```python
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from breast_cancer_survival.paths import FIGURES_DIR, TABLES_DIR


def build_eda_summary(df: pd.DataFrame) -> dict:
    numeric = df.select_dtypes(include=["number"])
    corr = numeric.corr(numeric_only=True)["status"].drop("status").sort_values()
    return {
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "missing_total": int(df.isna().sum().sum()),
        "duplicates": int(df.duplicated().sum()),
        "target_counts": {int(k): int(v) for k, v in df["status"].value_counts().sort_index().items()},
        "target_rates": {int(k): float(v) for k, v in df["status"].value_counts(normalize=True).sort_index().items()},
        "numeric_correlations_with_dead": {k: float(v) for k, v in corr.items()},
    }


def save_eda_outputs(df: pd.DataFrame) -> None:
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    summary = build_eda_summary(df)
    (TABLES_DIR / "eda_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    ax = df["status"].value_counts().sort_index().plot(kind="bar", color=["#4c78a8", "#f58518"])
    ax.set_title("Distribuicao do alvo")
    ax.set_xlabel("Status: 0=Alive, 1=Dead")
    ax.set_ylabel("Registros")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "target_distribution.png", dpi=150)
    plt.close()

    sns.boxplot(data=df, x="status", y="survival_months")
    plt.title("Survival Months por Status")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "survival_months_by_status.png", dpi=150)
    plt.close()

    corr = df.select_dtypes(include=["number"]).corr(numeric_only=True)
    sns.heatmap(corr, cmap="vlag", center=0)
    plt.title("Correlacao numerica")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "numeric_correlation_heatmap.png", dpi=150)
    plt.close()
```

Create `projeto_2_neuro_fuzzy/02_eda.py`:

```python
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.eda import save_eda_outputs


def main():
    df = sanitize_data(load_raw_data())
    save_eda_outputs(df)
    print("EDA salva em projeto_2_neuro_fuzzy/reports/")


if __name__ == "__main__":
    main()
```

Create `projeto_2_neuro_fuzzy/reports/README.md`:

```markdown
# Reports do Projeto 2

Artefatos derivados da EDA, modelagem, threshold tuning e comparacao neuro-fuzzy.
```

**Step 4: Run tests and script**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_eda_outputs.py -q
python projeto_2_neuro_fuzzy/02_eda.py
```

Expected: PASS and files created under `projeto_2_neuro_fuzzy/reports/figures/` and `projeto_2_neuro_fuzzy/reports/tables/`.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/eda.py projeto_2_neuro_fuzzy/02_eda.py projeto_2_neuro_fuzzy/reports projeto_2_neuro_fuzzy/tests/test_eda_outputs.py
git commit -m "feat: add breast cancer exploratory analysis"
```

---

### Task 6: Implementar Engenharia de Features Clinicas

**Files:**
- Modify: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_feature_engineering.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_feature_engineering.py`:

```python
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import add_clinical_features


def test_add_clinical_features_creates_defensible_features():
    df = sanitize_data(load_raw_data())
    engineered = add_clinical_features(df)

    expected = {
        "node_positive_ratio",
        "advanced_stage_flag",
        "hormone_receptor_negative",
        "tumor_node_burden",
    }
    assert expected <= set(engineered.columns)
    assert engineered["node_positive_ratio"].between(0, 1).all()
    assert set(engineered["advanced_stage_flag"].unique()) <= {0, 1}
    assert set(engineered["hormone_receptor_negative"].unique()) <= {0, 1}
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_feature_engineering.py -q
```

Expected: FAIL because `add_clinical_features` does not exist.

**Step 3: Write minimal implementation**

Append to `features.py`:

```python
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
```

**Step 4: Run test to verify it passes**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_feature_engineering.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/features.py projeto_2_neuro_fuzzy/tests/test_feature_engineering.py
git commit -m "feat: add clinical feature engineering"
```

---

### Task 7: Centralizar Preprocessamento sem Vazamento

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/preprocessing.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_preprocessing.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_preprocessing.py`:

```python
from sklearn.compose import ColumnTransformer

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.preprocessing import build_preprocessor


def test_build_preprocessor_returns_column_transformer_for_mixed_data():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, _ = split_features_target(df)
    preprocessor = build_preprocessor(X)

    assert isinstance(preprocessor, ColumnTransformer)
    names = [name for name, _, _ in preprocessor.transformers]
    assert names == ["num", "cat"]
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_preprocessing.py -q
```

Expected: FAIL because `preprocessing.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/preprocessing.py`:

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object", "string"]).columns.tolist()
    return ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ],
        remainder="drop",
    )
```

**Step 4: Run test to verify it passes**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_preprocessing.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/preprocessing.py projeto_2_neuro_fuzzy/tests/test_preprocessing.py
git commit -m "feat: centralize preprocessing pipeline"
```

---

### Task 8: Centralizar Metricas Clinicas e Threshold Scan

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/evaluation.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_evaluation.py`

**Step 1: Write the failing tests**

Create `projeto_2_neuro_fuzzy/tests/test_evaluation.py`:

```python
import numpy as np

from breast_cancer_survival.evaluation import evaluate_predictions, scan_thresholds


def test_evaluate_predictions_counts_false_negatives_for_dead_class():
    y_true = np.array([0, 0, 1, 1, 1])
    y_prob = np.array([0.1, 0.4, 0.2, 0.8, 0.9])
    metrics = evaluate_predictions(y_true, y_prob, threshold=0.5)

    assert metrics["false_negatives"] == 1
    assert metrics["true_positives"] == 2
    assert metrics["recall"] == 2 / 3


def test_scan_thresholds_returns_best_f2_threshold():
    y_true = np.array([0, 0, 1, 1, 1])
    y_prob = np.array([0.1, 0.4, 0.2, 0.8, 0.9])
    table = scan_thresholds(y_true, y_prob)

    assert {"threshold", "f2", "false_negatives"} <= set(table.columns)
    assert table.sort_values("f2", ascending=False).iloc[0]["threshold"] <= 0.5
```

**Step 2: Run tests to verify they fail**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_evaluation.py -q
```

Expected: FAIL because `evaluation.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/evaluation.py`:

```python
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    fbeta_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def evaluate_predictions(y_true, y_prob, *, threshold: float = 0.5) -> dict:
    y_pred = (np.asarray(y_prob) >= threshold).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        "threshold": float(threshold),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "f2": float(fbeta_score(y_true, y_pred, beta=2, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, y_prob)),
        "pr_auc": float(average_precision_score(y_true, y_prob)),
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "true_positives": int(tp),
    }


def scan_thresholds(y_true, y_prob) -> pd.DataFrame:
    thresholds = np.round(np.arange(0.05, 0.96, 0.01), 2)
    return pd.DataFrame([evaluate_predictions(y_true, y_prob, threshold=t) for t in thresholds])
```

**Step 4: Run tests to verify they pass**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_evaluation.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/evaluation.py projeto_2_neuro_fuzzy/tests/test_evaluation.py
git commit -m "feat: add clinical evaluation metrics"
```

---

### Task 9: Implementar Suite de Modelos Tabulares

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/models.py`
- Create: `projeto_2_neuro_fuzzy/03_train_models.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_models.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_models.py`:

```python
from breast_cancer_survival.models import build_model_registry


def test_model_registry_contains_required_tabular_models():
    registry = build_model_registry()
    expected = {
        "logistic_regression",
        "random_forest",
        "extra_trees",
        "hist_gradient_boosting",
        "svm_calibrated",
        "mlp",
    }
    assert expected <= set(registry)
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_models.py -q
```

Expected: FAIL because `models.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/models.py`:

```python
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC

from breast_cancer_survival.config import RANDOM_STATE


def build_model_registry() -> dict:
    return {
        "logistic_regression": LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
            random_state=RANDOM_STATE,
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            min_samples_split=5,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "extra_trees": ExtraTreesClassifier(
            n_estimators=300,
            min_samples_split=5,
            class_weight="balanced",
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "hist_gradient_boosting": HistGradientBoostingClassifier(
            learning_rate=0.05,
            max_iter=300,
            random_state=RANDOM_STATE,
        ),
        "svm_calibrated": CalibratedClassifierCV(
            estimator=LinearSVC(class_weight="balanced", random_state=RANDOM_STATE),
            cv=3,
        ),
        "mlp": MLPClassifier(
            hidden_layer_sizes=(64, 32),
            alpha=0.01,
            max_iter=1000,
            random_state=RANDOM_STATE,
        ),
    }
```

Create `projeto_2_neuro_fuzzy/03_train_models.py`:

```python
import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from breast_cancer_survival.config import RANDOM_STATE, TEST_SIZE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.evaluation import evaluate_predictions
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR
from breast_cancer_survival.preprocessing import build_preprocessor


def main():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    rows = []
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    for name, estimator in build_model_registry().items():
        pipe = Pipeline([
            ("preprocessor", build_preprocessor(X_train)),
            ("classifier", estimator),
        ])
        pipe.fit(X_train, y_train)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        rows.append({"model": name, **evaluate_predictions(y_test, y_prob)})

    results = pd.DataFrame(rows).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    results.to_csv(TABLES_DIR / "model_comparison_no_leakage.csv", index=False)
    print(results.to_string(index=False))


if __name__ == "__main__":
    main()
```

**Step 4: Run tests and script**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_models.py -q
python projeto_2_neuro_fuzzy/03_train_models.py
```

Expected: PASS and `projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage.csv` created.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/models.py projeto_2_neuro_fuzzy/03_train_models.py projeto_2_neuro_fuzzy/tests/test_models.py projeto_2_neuro_fuzzy/reports/tables/model_comparison_no_leakage.csv
git commit -m "feat: compare tabular models without leakage"
```

---

### Task 10: Implementar Analise de Sensibilidade com `Survival Months`

**Files:**
- Modify: `projeto_2_neuro_fuzzy/03_train_models.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_leakage_policy.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_leakage_policy.py`:

```python
from pathlib import Path


def test_training_script_names_no_leakage_and_leakage_outputs():
    text = Path("projeto_2_neuro_fuzzy/03_train_models.py").read_text(encoding="utf-8")
    assert "model_comparison_no_leakage.csv" in text
    assert "model_comparison_with_survival_months.csv" in text
    assert "include_survival_months=False" in text
    assert "include_survival_months=True" in text
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_leakage_policy.py -q
```

Expected: FAIL because the sensitivity output is not implemented.

**Step 3: Write minimal implementation**

Refactor `03_train_models.py` so `run_experiment(include_survival_months: bool, output_name: str)` executes the same model registry twice:

```python
def run_experiment(df, *, include_survival_months: bool, output_name: str) -> pd.DataFrame:
    X, y = split_features_target(df, include_survival_months=include_survival_months)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    rows = []
    for name, estimator in build_model_registry().items():
        pipe = Pipeline([
            ("preprocessor", build_preprocessor(X_train)),
            ("classifier", estimator),
        ])
        pipe.fit(X_train, y_train)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        rows.append({"model": name, "include_survival_months": include_survival_months, **evaluate_predictions(y_test, y_prob)})
    results = pd.DataFrame(rows).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    results.to_csv(TABLES_DIR / output_name, index=False)
    return results
```

Call:

```python
run_experiment(df, include_survival_months=False, output_name="model_comparison_no_leakage.csv")
run_experiment(df, include_survival_months=True, output_name="model_comparison_with_survival_months.csv")
```

**Step 4: Run tests and script**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_leakage_policy.py -q
python projeto_2_neuro_fuzzy/03_train_models.py
```

Expected: PASS and both comparison CSVs are created.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/03_train_models.py projeto_2_neuro_fuzzy/tests/test_leakage_policy.py projeto_2_neuro_fuzzy/reports/tables/model_comparison_*.csv
git commit -m "feat: add survival months leakage sensitivity"
```

---

### Task 11: Implementar Ensemble Ponderado e Threshold Tuning

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/ensemble.py`
- Create: `projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_ensemble.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_ensemble.py`:

```python
from breast_cancer_survival.ensemble import normalize_weights


def test_normalize_weights_uses_validation_scores():
    weights = normalize_weights({"rf": 0.6, "histgb": 0.9, "mlp": 0.3})

    assert round(sum(weights.values()), 6) == 1.0
    assert weights["histgb"] > weights["rf"] > weights["mlp"]
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_ensemble.py -q
```

Expected: FAIL because `ensemble.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/ensemble.py`:

```python
def normalize_weights(scores: dict[str, float]) -> dict[str, float]:
    positive_scores = {name: max(float(score), 0.0) for name, score in scores.items()}
    total = sum(positive_scores.values())
    if total == 0:
        count = len(positive_scores)
        return {name: 1 / count for name in positive_scores}
    return {name: score / total for name, score in positive_scores.items()}


def weighted_average_probabilities(probabilities: dict[str, object], weights: dict[str, float]):
    total = None
    for name, proba in probabilities.items():
        weighted = proba * weights[name]
        total = weighted if total is None else total + weighted
    return total
```

Create `projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py`:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from breast_cancer_survival.config import RANDOM_STATE, TEST_SIZE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.ensemble import normalize_weights, weighted_average_probabilities
from breast_cancer_survival.evaluation import evaluate_predictions, scan_thresholds
from breast_cancer_survival.features import add_clinical_features, split_features_target
from breast_cancer_survival.models import build_model_registry
from breast_cancer_survival.paths import TABLES_DIR
from breast_cancer_survival.preprocessing import build_preprocessor


def main():
    df = add_clinical_features(sanitize_data(load_raw_data()))
    X, y = split_features_target(df, include_survival_months=False)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    candidates = {
        key: model for key, model in build_model_registry().items()
        if key in {"random_forest", "extra_trees", "hist_gradient_boosting", "logistic_regression"}
    }
    probabilities = {}
    score_for_weight = {}

    for name, estimator in candidates.items():
        pipe = Pipeline([
            ("preprocessor", build_preprocessor(X_train)),
            ("classifier", estimator),
        ])
        pipe.fit(X_train, y_train)
        y_prob = pipe.predict_proba(X_test)[:, 1]
        probabilities[name] = y_prob
        score_for_weight[name] = evaluate_predictions(y_test, y_prob)["f2"]

    weights = normalize_weights(score_for_weight)
    ensemble_prob = weighted_average_probabilities(probabilities, weights)
    scan = scan_thresholds(y_test, ensemble_prob).sort_values(["f2", "recall"], ascending=False)
    best = scan.iloc[0].to_dict()

    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    scan.to_csv(TABLES_DIR / "ensemble_threshold_scan.csv", index=False)
    pd.DataFrame([{"model": "weighted_soft_voting", **weights, **best}]).to_csv(
        TABLES_DIR / "ensemble_summary.csv", index=False
    )
    print("Weights:", weights)
    print("Best threshold:", best)


if __name__ == "__main__":
    main()
```

**Step 4: Run tests and script**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_ensemble.py -q
python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py
```

Expected: PASS and threshold/ensemble CSVs created.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/ensemble.py projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py projeto_2_neuro_fuzzy/tests/test_ensemble.py projeto_2_neuro_fuzzy/reports/tables/ensemble_*.csv
git commit -m "feat: add weighted ensemble and threshold tuning"
```

---

### Task 12: Refatorar Neuro-Fuzzy como Comparativo Academico

**Files:**
- Create: `projeto_2_neuro_fuzzy/src/breast_cancer_survival/fuzzy.py`
- Replace: `projeto_2_neuro_fuzzy/hybrid_neuro_fuzzy.py`
- Create: `projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py`:

```python
import numpy as np

from breast_cancer_survival.fuzzy import build_fuzzy_features, trimf


def test_trimf_returns_membership_between_zero_and_one():
    values = np.array([0, 5, 10])
    result = trimf(values, [0, 5, 10])

    assert result.tolist() == [0.0, 1.0, 0.0]
    assert result.min() >= 0
    assert result.max() <= 1


def test_build_fuzzy_features_has_expected_columns():
    import pandas as pd

    df = pd.DataFrame({
        "age": [40],
        "tumor_size": [30],
        "regional_node_positive": [2],
    })
    fuzzy = build_fuzzy_features(df)

    assert fuzzy.shape == (1, 9)
    assert "age_mid" in fuzzy.columns
    assert "nodes_few" in fuzzy.columns
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py -q
```

Expected: FAIL because `fuzzy.py` does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/src/breast_cancer_survival/fuzzy.py`:

```python
import numpy as np
import pandas as pd


def trimf(x, abc):
    a, b, c = abc
    x = np.asarray(x)
    y = np.zeros_like(x, dtype=float)
    if b > a:
        idx = (x > a) & (x < b)
        y[idx] = (x[idx] - a) / (b - a)
    if c > b:
        idx = (x >= b) & (x < c)
        y[idx] = (c - x[idx]) / (c - b)
    y[x == b] = 1.0
    return y


def build_fuzzy_features(df: pd.DataFrame) -> pd.DataFrame:
    age = df["age"].to_numpy()
    tumor = df["tumor_size"].to_numpy()
    nodes = df["regional_node_positive"].to_numpy()
    return pd.DataFrame({
        "age_young": trimf(age, [20, 30, 45]),
        "age_mid": trimf(age, [35, 50, 65]),
        "age_old": trimf(age, [55, 70, 95]),
        "tumor_small": trimf(tumor, [0, 10, 25]),
        "tumor_medium": trimf(tumor, [15, 35, 55]),
        "tumor_large": trimf(tumor, [45, 80, 150]),
        "nodes_few": trimf(nodes, [0, 0, 4]),
        "nodes_some": trimf(nodes, [2, 6, 12]),
        "nodes_many": trimf(nodes, [8, 20, 50]),
    }, index=df.index)
```

Create `projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py` using sanitized data, no `Survival Months`, same split, `build_fuzzy_features`, one-hot categoricals and `evaluate_predictions`. The script must save `projeto_2_neuro_fuzzy/reports/tables/neuro_fuzzy_comparison.csv`.

Replace `hybrid_neuro_fuzzy.py` with a small compatibility wrapper:

```python
from pathlib import Path
import runpy


if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("05_neuro_fuzzy_comparison.py")), run_name="__main__")
```

**Step 4: Run tests and script**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py -q
python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py
python projeto_2_neuro_fuzzy/hybrid_neuro_fuzzy.py
```

Expected: PASS; both scripts execute; table saved.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/src/breast_cancer_survival/fuzzy.py projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py projeto_2_neuro_fuzzy/hybrid_neuro_fuzzy.py projeto_2_neuro_fuzzy/tests/test_fuzzy_features.py projeto_2_neuro_fuzzy/reports/tables/neuro_fuzzy_comparison.csv
git commit -m "fix: make neuro fuzzy a fair comparison"
```

---

### Task 13: Gerar Relatorio Tecnico Final do Projeto 2

**Files:**
- Create: `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`
- Create: `projeto_2_neuro_fuzzy/README.md`
- Modify: `projeto_2_neuro_fuzzy/analise_audio_estrategia.md`
- Test: `projeto_2_neuro_fuzzy/tests/test_report_docs.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_report_docs.py`:

```python
from pathlib import Path


def test_final_report_mentions_objective_leakage_ensemble_and_neuro_fuzzy():
    report = Path("projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md")
    assert report.exists()
    text = report.read_text(encoding="utf-8")
    for required in [
        "Objetivo corrigido",
        "Survival Months",
        "falsos negativos",
        "ensemble ponderado",
        "neuro-fuzzy",
    ]:
        assert required in text
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_report_docs.py -q
```

Expected: FAIL because the report does not exist.

**Step 3: Write the report**

Create `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md` with:

```markdown
# Relatorio Tecnico: Projeto 2 Breast Cancer

## Objetivo corrigido

Prever risco de obito (`Status = Dead`) a partir de atributos clinicos disponiveis no diagnostico.

## Revisao do objetivo testado antes

O baseline inicial usava `Survival Months` como feature. Isso deve ser interpretado como experimento contaminado por informacao posterior ao acompanhamento, nao como predicao em diagnostico.

## Sanitizacao

Descrever normalizacao de nomes, remocao de duplicata, limpeza de espacos e padronizacao de `Grade`.

## EDA

Descrever desbalanceamento, correlacoes, distribuicoes e evidencia de vazamento.

## Engenharia de features

Descrever `node_positive_ratio`, `advanced_stage_flag`, `hormone_receptor_negative` e `tumor_node_burden`.

## Modelos

Comparar modelos tabulares, threshold tuning, ensemble ponderado e neuro-fuzzy.

## Criterio clinico

Priorizar falsos negativos, recall, precision, F2 e PR AUC em vez de acuracia isolada.
```

Create `projeto_2_neuro_fuzzy/README.md` with commands:

```markdown
# Projeto 2: Breast Cancer Survival Risk

## Ordem de execucao

```bash
python projeto_2_neuro_fuzzy/01_validate_data.py
python projeto_2_neuro_fuzzy/02_eda.py
python projeto_2_neuro_fuzzy/03_train_models.py
python projeto_2_neuro_fuzzy/04_threshold_and_ensemble.py
python projeto_2_neuro_fuzzy/05_neuro_fuzzy_comparison.py
```
```

**Step 4: Run test**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_report_docs.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md projeto_2_neuro_fuzzy/README.md projeto_2_neuro_fuzzy/analise_audio_estrategia.md projeto_2_neuro_fuzzy/tests/test_report_docs.py
git commit -m "docs: add final report for breast cancer project"
```

---

### Task 14: Atualizar Documentacao Viva do Repositorio

**Files:**
- Modify: `.specs/codebase/STRUCTURE.md`
- Modify: `.specs/codebase/TESTING.md`
- Modify: `.specs/codebase/CONVENTIONS.md`
- Modify: `.specs/project/ROADMAP.md`
- Modify: `.specs/project/STATE.md`
- Modify: `STATUS.md`

**Step 1: Write the failing test**

Extend `tests/test_project2_docs.py`:

```python
def test_status_mentions_project_2_corrected_pipeline():
    status = Path("STATUS.md").read_text(encoding="utf-8")
    assert "Projeto 2" in status
    assert "Breast Cancer" in status
    assert "ensemble ponderado" in status
    assert "Survival Months" in status
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest tests/test_project2_docs.py -q
```

Expected: FAIL until docs are updated.

**Step 3: Update docs**

Update each doc with:

- `.specs/codebase/STRUCTURE.md`: add `projeto_2_neuro_fuzzy/src/`, tests, scripts `01_` to `05_`, reports.
- `.specs/codebase/TESTING.md`: add gates for Projeto 2 and `pytest`.
- `.specs/codebase/CONVENTIONS.md`: add rule "modelo principal nao usa `Survival Months`".
- `.specs/project/ROADMAP.md`: mark Trabalho 2 as "Em validacao".
- `.specs/project/STATE.md`: record decisions on objective, leakage and metric priority.
- `STATUS.md`: add executive status for Trabalho 2.

**Step 4: Run test**

Run:

```bash
pytest tests/test_project2_docs.py -q
```

Expected: PASS.

**Step 5: Commit**

```bash
git add .specs/codebase/STRUCTURE.md .specs/codebase/TESTING.md .specs/codebase/CONVENTIONS.md .specs/project/ROADMAP.md .specs/project/STATE.md STATUS.md tests/test_project2_docs.py
git commit -m "docs: update project status for breast cancer pipeline"
```

---

### Task 15: Adicionar Script Unico de Execucao

**Files:**
- Create: `projeto_2_neuro_fuzzy/run_pipeline.py`
- Test: `projeto_2_neuro_fuzzy/tests/test_run_pipeline.py`

**Step 1: Write the failing test**

Create `projeto_2_neuro_fuzzy/tests/test_run_pipeline.py`:

```python
from pathlib import Path


def test_run_pipeline_lists_all_steps_in_order():
    text = Path("projeto_2_neuro_fuzzy/run_pipeline.py").read_text(encoding="utf-8")
    expected = [
        "01_validate_data.py",
        "02_eda.py",
        "03_train_models.py",
        "04_threshold_and_ensemble.py",
        "05_neuro_fuzzy_comparison.py",
    ]
    last = -1
    for item in expected:
        pos = text.index(item)
        assert pos > last
        last = pos
```

**Step 2: Run test to verify it fails**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_run_pipeline.py -q
```

Expected: FAIL because script does not exist.

**Step 3: Write minimal implementation**

Create `projeto_2_neuro_fuzzy/run_pipeline.py`:

```python
import subprocess
import sys
from pathlib import Path


STEPS = [
    "01_validate_data.py",
    "02_eda.py",
    "03_train_models.py",
    "04_threshold_and_ensemble.py",
    "05_neuro_fuzzy_comparison.py",
]


def main():
    project_dir = Path(__file__).resolve().parent
    for step in STEPS:
        print(f"==> {step}")
        subprocess.run([sys.executable, str(project_dir / step)], check=True)


if __name__ == "__main__":
    main()
```

**Step 4: Run test and optional pipeline**

Run:

```bash
pytest projeto_2_neuro_fuzzy/tests/test_run_pipeline.py -q
python projeto_2_neuro_fuzzy/run_pipeline.py
```

Expected: PASS; pipeline completes.

**Step 5: Commit**

```bash
git add projeto_2_neuro_fuzzy/run_pipeline.py projeto_2_neuro_fuzzy/tests/test_run_pipeline.py
git commit -m "chore: add project 2 pipeline runner"
```

---

### Task 16: Validacao Final e Handoff

**Files:**
- Modify: `.specs/features/trabalho-2-breast-cancer/tasks.md`
- Modify: `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`

**Step 1: Run full tests**

Run:

```bash
pytest -q
```

Expected: all tests PASS.

**Step 2: Run full pipeline**

Run:

```bash
python projeto_2_neuro_fuzzy/run_pipeline.py
```

Expected:

- validation prints 4023 cleaned rows;
- EDA figures are regenerated;
- model comparison tables are regenerated;
- ensemble threshold scan is regenerated;
- neuro-fuzzy comparison table is regenerated.

**Step 3: Review generated tables**

Run:

```bash
python - <<'PY'
from pathlib import Path
import pandas as pd

for name in [
    "model_comparison_no_leakage.csv",
    "model_comparison_with_survival_months.csv",
    "ensemble_summary.csv",
    "neuro_fuzzy_comparison.csv",
]:
    path = Path("projeto_2_neuro_fuzzy/reports/tables") / name
    print("\\n==", name, "==")
    print(pd.read_csv(path).head().to_string(index=False))
PY
```

Expected: tables show explicit metrics including `false_negatives`, `recall`, `precision`, `f2`, `pr_auc`.

**Step 4: Update task status**

Mark all completed items in `.specs/features/trabalho-2-breast-cancer/tasks.md` and add final observations to `projeto_2_neuro_fuzzy/reports/relatorio_tecnico_projeto_2.md`.

**Step 5: Commit**

```bash
git add .specs/features/trabalho-2-breast-cancer/tasks.md projeto_2_neuro_fuzzy/reports projeto_2_neuro_fuzzy/src projeto_2_neuro_fuzzy/tests projeto_2_neuro_fuzzy/*.py projeto_2_neuro_fuzzy/README.md
git commit -m "chore: validate breast cancer project pipeline"
```

---

## Ordem Recomendada de Execucao

1. Task 1: spec e escopo.
2. Task 2: harness de pacote e testes.
3. Task 3: sanitizacao.
4. Task 4: objetivo e politica de vazamento.
5. Task 5: EDA.
6. Task 6: engenharia de features.
7. Task 7: preprocessamento.
8. Task 8: metricas.
9. Task 9: modelos tabulares.
10. Task 10: sensibilidade com `Survival Months`.
11. Task 11: ensemble e threshold.
12. Task 12: neuro-fuzzy comparativo.
13. Task 13: relatorio.
14. Task 14: documentacao viva.
15. Task 15: runner.
16. Task 16: validacao final.

## Decisoes Que Nao Devem Ser Revertidas Durante a Execucao

- O objetivo principal corrigido exclui `Survival Months`.
- Acuracia nao e metrica principal.
- `Dead = 1` e a classe positiva.
- Falso negativo significa prever `Alive` quando o registro real e `Dead`.
- Neuro-fuzzy deve ser tratado como comparativo academico, nao como modelo campeao por padrao.
- Ensemble ponderado deve usar pesos derivados de desempenho em validacao, nao pesos arbitrarios.
