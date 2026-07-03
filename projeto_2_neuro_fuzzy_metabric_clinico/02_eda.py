from pathlib import Path
import sys


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.eda import save_eda_outputs
from breast_cancer_survival.paths import REPORTS_DIR, ensure_output_dirs


def main():
    ensure_output_dirs()
    raw = load_raw_data()
    clean = sanitize_data(raw)
    save_eda_outputs(raw, clean)
    print(f"EDA outputs saved under: {REPORTS_DIR}")


if __name__ == "__main__":
    main()

