import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / \
    "data" / "ibm_hr_attrition.csv"


def load_data() -> pd.DataFrame:
    raw_data = pd.read_csv(DATA_PATH, encoding='UTF-8')
    df = raw_data.copy()
    df = df.drop_duplicates()
    return df
