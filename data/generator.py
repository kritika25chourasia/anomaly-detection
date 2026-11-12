import numpy as np
import pandas as pd


def make_series(days=14, seed=0):
    rng = np.random.default_rng(seed)
    index = pd.date_range("2026-01-01", periods=days * 1440, freq="min")
    t = np.arange(len(index))
    value = 50 + 20 * np.sin(2 * np.pi * t / 1440) + rng.normal(0, 3, len(t))
    return pd.DataFrame({"value": value, "label": 0}, index=index)


def inject_anomalies(df, seed=1, n=12):
    df = df.copy()
    rng = np.random.default_rng(seed)
    df["kind"] = "normal"

    vcol = df.columns.get_loc("value")
    lcol = df.columns.get_loc("label")
    kcol = df.columns.get_loc("kind")

    lengths = {"spike": 5, "drop": 5, "stuck": 30, "drift": 120}
    start_of_usable = 1440
    slot = (len(df) - start_of_usable) // n

    for i in range(n):
        kind = rng.choice(list(lengths))
        length = lengths[kind]

        low = start_of_usable + i * slot + 50
        high = start_of_usable + (i + 1) * slot - length - 50
        start = int(rng.integers(low, high))
        end = start + length

        if kind == "spike":
            df.iloc[start:end, vcol] += 40
        elif kind == "drop":
            df.iloc[start:end, vcol] -= 40
        elif kind == "stuck":
            df.iloc[start:end, vcol] = df.iloc[start, vcol]
        else:
            df.iloc[start:end, vcol] += np.linspace(0, 30, length)

        df.iloc[start:end, lcol] = 1
        df.iloc[start:end, kcol] = kind

    return df


def make_dataset(seed=0):
    return inject_anomalies(make_series(seed=seed), seed=seed + 100)