from pathlib import Path
import sys

import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline


PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR / "src"))

from breast_cancer_survival.config import RANDOM_STATE
from breast_cancer_survival.data import load_raw_data, sanitize_data
from breast_cancer_survival.evaluation import evaluate_predictions
from breast_cancer_survival.features import split_features_target
from breast_cancer_survival.fuzzy import build_fuzzy_features
from breast_cancer_survival.paths import TABLES_DIR, ensure_output_dirs
from breast_cancer_survival.preprocessing import build_preprocessor
from breast_cancer_survival.splits import make_holdout_split


def build_neuro_fuzzy_frame(df: pd.DataFrame) -> pd.DataFrame:
    X_base, _ = split_features_target(df, include_survival_months=False)
    fuzzy = build_fuzzy_features(df)
    categorical = X_base.select_dtypes(include=["object", "string"]).copy()
    numeric_passthrough = X_base[["grade", "regional_node_examined"]].copy()
    return pd.concat([fuzzy, numeric_passthrough, categorical], axis=1)


def main():
    ensure_output_dirs()
    df = sanitize_data(load_raw_data())
    X = build_neuro_fuzzy_frame(df)
    y = df["status"]
    split = make_holdout_split(X, y)
    pipe = Pipeline(
        [
            ("preprocessor", build_preprocessor(split.X_train)),
            (
                "classifier",
                MLPClassifier(
                    hidden_layer_sizes=(64, 32),
                    alpha=0.01,
                    max_iter=700,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )
    pipe.fit(split.X_train, split.y_train)
    y_prob = pipe.predict_proba(split.X_test)[:, 1]
    result = pd.DataFrame(
        [
            {
                "model": "cooperative_neuro_fuzzy_mlp",
                "note": "manual fuzzy membership features plus MLP; not full ANFIS",
                **evaluate_predictions(split.y_test, y_prob),
            }
        ]
    )
    result.to_csv(TABLES_DIR / "neuro_fuzzy_comparison.csv", index=False)
    print(result.to_string(index=False))


if __name__ == "__main__":
    main()
