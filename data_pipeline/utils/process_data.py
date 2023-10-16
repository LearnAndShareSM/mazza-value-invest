import numpy as np
from utils.constants import MIN_BIGINT, MAX_BIGINT


def filter_bigint_range(df):
    min_bigint = -MIN_BIGINT
    max_bigint = MAX_BIGINT

    for col in df.select_dtypes(include=[np.number]).columns:
        mask = (df[col] >= min_bigint) & (df[col] <= max_bigint)
        df = df[mask]

    return df
