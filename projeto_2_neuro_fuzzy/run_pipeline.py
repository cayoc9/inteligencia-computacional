import subprocess
import sys
from pathlib import Path


STEPS = [
    "01_validate_data.py",
    "02_eda.py",
    "03_train_models.py",
    "04_threshold_and_ensemble.py",
    "05_neuro_fuzzy_comparison.py",
    "06_explainability.py",
    "07_stability_analysis.py",
]


def main():
    project_dir = Path(__file__).resolve().parent
    for step in STEPS:
        print(f"==> {step}")
        subprocess.run([sys.executable, str(project_dir / step)], check=True)


if __name__ == "__main__":
    main()
