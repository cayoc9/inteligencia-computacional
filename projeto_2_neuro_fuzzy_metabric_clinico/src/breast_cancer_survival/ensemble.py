import numpy as np
import pandas as pd

from breast_cancer_survival.evaluation import scan_thresholds, summarize_threshold_scenarios


def normalize_weights(scores: dict[str, float]) -> dict[str, float]:
    positive_scores = {name: max(float(score), 0.0) for name, score in scores.items()}
    total = sum(positive_scores.values())
    if total == 0:
        count = len(positive_scores)
        return {name: 1 / count for name in positive_scores}
    return {name: score / total for name, score in positive_scores.items()}


def weighted_average_probabilities(probabilities: dict[str, np.ndarray], weights: dict[str, float]) -> np.ndarray:
    total = None
    for name, proba in probabilities.items():
        weighted = np.asarray(proba) * weights[name]
        total = weighted if total is None else total + weighted
    return total


def build_validation_weight_table(y_true, probabilities: dict[str, np.ndarray]) -> pd.DataFrame:
    rows = []
    for name, y_prob in probabilities.items():
        scenarios = summarize_threshold_scenarios(y_true, y_prob)
        max_f2 = scenarios.loc[scenarios["scenario"] == "max_f2"].iloc[0]
        rows.append(
            {
                "model": name,
                "validation_f2": float(max_f2["f2"]),
                "validation_recall": float(max_f2["recall"]),
                "validation_pr_auc": float(max_f2["pr_auc"]),
                "validation_brier_score": float(max_f2["brier_score"]),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["validation_f2", "validation_recall", "validation_pr_auc"],
        ascending=False,
    )


def select_threshold_from_validation(y_true, y_prob) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    scan = scan_thresholds(y_true, y_prob).sort_values(["f2", "recall", "pr_auc"], ascending=False)
    scenarios = summarize_threshold_scenarios(y_true, y_prob)
    best = scan.iloc[0].to_dict()
    return scan, scenarios, best
