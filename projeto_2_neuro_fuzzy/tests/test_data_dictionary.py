from pathlib import Path

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.dictionary import build_data_dictionary, write_data_dictionary


def test_data_dictionary_covers_raw_columns_and_leakage(tmp_path):
    raw = load_raw_data()
    clean = sanitize_data(raw)
    dictionary = build_data_dictionary(raw, clean)

    assert len(dictionary[dictionary["raw_column"] != ""]) == len(raw.columns)
    assert "survival_months" in set(dictionary["sanitized_column"])
    survival = dictionary[dictionary["sanitized_column"] == "survival_months"].iloc[0]
    assert survival["role"] == "excluded_primary_model"
    assert "leakage" in survival["leakage_risk"]

    out = tmp_path / "DATA_DICTIONARY.md"
    write_data_dictionary(dictionary, out)
    text = out.read_text(encoding="utf-8")
    assert "Survival Months" in text
    assert "regional_node_positive" in text
    assert "node_positive_ratio" in text

