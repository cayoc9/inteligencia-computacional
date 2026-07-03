from pathlib import Path
import json
import sys


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.data import build_dataset_contract, load_raw_data, sanitize_data
from breast_cancer_survival.dictionary import build_data_dictionary, write_data_dictionary
from breast_cancer_survival.paths import DOCS_DIR, TABLES_DIR, ensure_output_dirs


def main():
    ensure_output_dirs()
    raw = load_raw_data()
    clean = sanitize_data(raw)
    contract = build_dataset_contract(raw, clean)
    dictionary = build_data_dictionary(raw, clean)

    write_data_dictionary(dictionary, DOCS_DIR / "DATA_DICTIONARY.md")
    (TABLES_DIR / "data_quality_summary.json").write_text(
        json.dumps(contract, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("Raw shape:", raw.shape)
    print("Clean shape:", clean.shape)
    print("Missing values:", contract["clean_missing_total"])
    print("Raw duplicates:", contract["raw_duplicates"])
    print("Clean duplicates:", contract["clean_duplicates"])
    print("Target counts:")
    print(clean["status"].value_counts().sort_index())
    print(f"Data dictionary: {DOCS_DIR / 'DATA_DICTIONARY.md'}")


if __name__ == "__main__":
    main()

