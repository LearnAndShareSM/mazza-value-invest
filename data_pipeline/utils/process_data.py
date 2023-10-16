import numpy as np


def filter_bigint_range(df):
    min_bigint = -9223372036854775808
    max_bigint = 9223372036854775807

    for col in df.select_dtypes(include=[np.number]).columns:
        mask = (df[col] >= min_bigint) & (df[col] <= max_bigint)
        df = df[mask]

    return df
