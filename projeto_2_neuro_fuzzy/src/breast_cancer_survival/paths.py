from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECT_DIR = REPO_ROOT / "projeto_2_neuro_fuzzy"
DATASET_PATH = PROJECT_DIR / "dataset" / "Breast_Cancer.csv"
DOCS_DIR = PROJECT_DIR / "docs"
REPORTS_DIR = PROJECT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
TABLES_DIR = REPORTS_DIR / "tables"
MODELS_DIR = PROJECT_DIR / "models"
NOTEBOOKS_DIR = PROJECT_DIR / "notebooks"


def ensure_output_dirs() -> None:
    for path in [DOCS_DIR, FIGURES_DIR, TABLES_DIR, MODELS_DIR, NOTEBOOKS_DIR]:
        path.mkdir(parents=True, exist_ok=True)

