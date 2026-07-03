import numpy as np


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

