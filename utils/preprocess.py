# utils/preprocess.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.dropna(inplace=True)
    df = df.reset_index(drop=True)
    return df
