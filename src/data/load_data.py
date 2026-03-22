import os
import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load the credit-g dataset from file system and return as pandas DataFrame."""


    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}. Please ensure the dataset is downloaded and placed in the correct directory.")

    return pd.read_csv(file_path)