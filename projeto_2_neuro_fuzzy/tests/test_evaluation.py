import numpy as np

from breast_cancer_survival.evaluation import evaluate_predictions, scan_thresholds


def test_evaluate_predictions_counts_false_negatives_for_dead_class():
    y_true = np.array([0, 0, 1, 1, 1])
    y_prob = np.array([0.1, 0.4, 0.2, 0.8, 0.9])
    metrics = evaluate_predictions(y_true, y_prob, threshold=0.5)

    assert metrics["false_negatives"] == 1
    assert metrics["true_positives"] == 2
    assert metrics["recall"] == 2 / 3


def test_scan_thresholds_returns_best_f2_threshold():
    y_true = np.array([0, 0, 1, 1, 1])
    y_prob = np.array([0.1, 0.4, 0.2, 0.8, 0.9])
    table = scan_thresholds(y_true, y_prob)

    assert {"threshold", "f2", "false_negatives"} <= set(table.columns)
    assert table.sort_values("f2", ascending=False).iloc[0]["threshold"] <= 0.5

