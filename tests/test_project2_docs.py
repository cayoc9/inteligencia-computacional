from pathlib import Path


def test_trabalho_2_spec_exists_and_defines_objective():
    spec = Path(".specs/features/trabalho-2-breast-cancer/spec.md")
    assert spec.exists()
    text = spec.read_text(encoding="utf-8")
    assert "Objetivo e Politica de Vazamento" in text
    assert "Survival Months" in text
    assert "falsos negativos" in text


def test_status_mentions_project_2_corrected_pipeline():
    status = Path("STATUS.md").read_text(encoding="utf-8")
    assert "Trabalho 2" in status
    assert "Projeto 2" in status
    assert "Breast Cancer" in status

