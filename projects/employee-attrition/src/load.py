import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / \
    "data" / "ibm_hr_attrition.csv"


def load_data():

    raw_data = pd.read_csv(DATA_PATH, encoding='UTF-8')

    return raw_data.copy()


df = load_data()


# Data Cleaning and Preprocessing
print('\nNumber Of Missing Values:', df.isnull().sum().sum())
print('Number Of Duplicate Rows:', df.duplicated().sum())

print('\n** Dropping Duplicate Rows **\n')
print('Initial Shape:', df.shape)

df = df.drop_duplicates()
print('New Shape:', df.shape)
