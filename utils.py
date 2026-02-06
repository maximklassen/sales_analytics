import pandas as pd
import os

def parse_date(series):
    """Safely parse a pandas Series to datetime."""
    return pd.to_datetime(series, errors="coerce")

def parse_float(series):
    """Safely parse a pandas Series to float."""
    return pd.to_numeric(series, errors="coerce")

def normalize_status(series):
    """
    Normalize order status values.
    Missing values are treated as 'completed'.
    """
    return series.fillna("completed").str.lower().str.strip()

def file_exists(file):
    """Ensure that a directory exists."""
    return os.path.isfile(file)