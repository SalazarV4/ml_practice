import os
import pandas as pd
from src.data.load_data import load_data

WORKING_DIR = os.environ["HOME"]
def test_load_data() -> None:

    file_path = "./ml_practice/data/raw/credit_score.csv"

    df = load_data(file_path=file_path)

    assert isinstance(df, pd.DataFrame)
