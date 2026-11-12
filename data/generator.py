import numpy as np
import pandas as pd

def make_series(days=14, seed=0):
    # 1. make a random number generator using the seed
    rng = np.random.default_rng(seed)

    # 2. make a time index: one timestamp per minute
    index = pd.date_range("2026-01-01", periods=days * 1440, freq="min")

    # 3. make t = 0, 1, 2, ... for each minute
    t = np.arange(len(index))

    # 4. build value = 50 + daily wave + noise
    value = 50 + 20 * np.sin(2 * np.pi * t / 1440) + rng.normal(0, 3, len(t))

    # 5. return a DataFrame with columns "value" and "label" (label all 0)
    return pd.DataFrame({"value": value, "label": 0}, index=index)