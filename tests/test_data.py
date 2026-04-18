import os
import pandas as pd
from src.data.load_data import load_data

WORKING_DIR = os.getcwd()
def test_load_data() -> None:

    file_path = f"{WORKING_DIR}/ml_practice/data/raw/credit_score.csv"

    df = load_data(file_path=file_path)

    assert isinstance(df, pd.DataFrame)
