from pathlib import Path

from breast_cancer_survival.paths import DATASET_PATH, REPORTS_DIR


def test_project_paths_resolve_inside_project():
    assert DATASET_PATH.name == "Breast_Cancer.csv"
    assert DATASET_PATH.exists()
    assert REPORTS_DIR == Path.cwd() / "projeto_2_neuro_fuzzy" / "reports"

