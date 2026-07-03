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
    nodes = df["lymph_nodes_positive"].fillna(0).to_numpy()
    npi = df["npi"].fillna(df["npi"].median()).to_numpy()
    return pd.DataFrame(
        {
            "age_young": trimf(age, [20, 35, 50]),
            "age_mid": trimf(age, [40, 55, 70]),
            "age_old": trimf(age, [60, 75, 95]),
            "tumor_small": trimf(tumor, [0, 10, 25]),
            "tumor_medium": trimf(tumor, [15, 35, 55]),
            "tumor_large": trimf(tumor, [45, 80, 150]),
            "nodes_none_or_few": trimf(nodes, [0, 0, 3]),
            "nodes_some": trimf(nodes, [1, 5, 12]),
            "nodes_many": trimf(nodes, [8, 20, 60]),
            "npi_low": trimf(npi, [0, 2.5, 4]),
            "npi_mid": trimf(npi, [3, 4.5, 6]),
            "npi_high": trimf(npi, [5, 7, 10]),
        },
        index=df.index,
    )
