import numpy as np
import pandas as pd


def trimf(x, abc):
    a, b, c = abc
    x = np.asarray(x)
    y = np.zeros_like(x, dtype=float)
    if b > a:
        idx = (x > a) & (x < b)
        y[idx] = (x[idx] - a) / (b - a)
    if c > b:
        idx = (x >= b) & (x < c)
        y[idx] = (c - x[idx]) / (c - b)
    y[x == b] = 1.0
    return y


def build_fuzzy_features(df: pd.DataFrame) -> pd.DataFrame:
    age = df["age"].to_numpy()
    tumor = df["tumor_size"].to_numpy()
    nodes = df["regional_node_positive"].to_numpy()
    return pd.DataFrame(
        {
            "age_young": trimf(age, [20, 30, 45]),
            "age_mid": trimf(age, [35, 50, 65]),
            "age_old": trimf(age, [55, 70, 95]),
            "tumor_small": trimf(tumor, [0, 10, 25]),
            "tumor_medium": trimf(tumor, [15, 35, 55]),
            "tumor_large": trimf(tumor, [45, 80, 150]),
            "nodes_few": trimf(nodes, [0, 0, 4]),
            "nodes_some": trimf(nodes, [2, 6, 12]),
            "nodes_many": trimf(nodes, [8, 20, 50]),
        },
        index=df.index,
    )

