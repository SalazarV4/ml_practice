import pandas as pd
from src.data.load_data import load_data

def test_load_data() -> None:
    file_path = "/workspaces/ml_practice/data/raw/credit_score.csv"

    df = load_data(file_path=file_path)

    assert isinstance(df, pd.DataFrame)


