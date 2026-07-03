from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    brier_score_loss,
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
        "brier_score": float(brier_score_loss(y_true, y_prob)),
        "clinical_utility": float((5 * tp) - (8 * fn) - fp),
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "true_positives": int(tp),
    }


def scan_thresholds(y_true, y_prob) -> pd.DataFrame:
    thresholds = np.round(np.arange(0.05, 0.96, 0.01), 2)
    return pd.DataFrame([evaluate_predictions(y_true, y_prob, threshold=t) for t in thresholds])


def summarize_threshold_scenarios(y_true, y_prob) -> pd.DataFrame:
    scan = scan_thresholds(y_true, y_prob)
    scenarios = []

    scenario_specs = {
        "max_f2": scan.sort_values(["f2", "recall", "pr_auc"], ascending=False),
        "max_recall": scan.sort_values(["recall", "precision", "pr_auc"], ascending=False),
        "max_clinical_utility": scan.sort_values(["clinical_utility", "f2"], ascending=False),
    }
    for name, table in scenario_specs.items():
        row = table.iloc[0].to_dict()
        row["scenario"] = name
        scenarios.append(row)

    precision_floor = scan[scan["precision"] >= 0.30]
    if not precision_floor.empty:
        row = precision_floor.sort_values(["recall", "f2", "pr_auc"], ascending=False).iloc[0].to_dict()
        row["scenario"] = "recall_with_precision_floor_0_30"
        scenarios.append(row)

    recall_floor = scan[scan["recall"] >= 0.80]
    if not recall_floor.empty:
        row = recall_floor.sort_values(["precision", "f2", "pr_auc"], ascending=False).iloc[0].to_dict()
        row["scenario"] = "precision_with_recall_floor_0_80"
        scenarios.append(row)

    columns = ["scenario"] + [col for col in scan.columns if col != "scenario"]
    return pd.DataFrame(scenarios)[columns]
