import pandas as pd
from src.load import load_data
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split


COLS_TO_DROP = ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours']


def prepare_features():
    df = load_data()
    df = df.drop(columns=COLS_TO_DROP)

    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    cat_columns = df.select_dtypes(include=['object']).columns.tolist()
    df_encoded = pd.get_dummies(df, columns=cat_columns, drop_first=True)

    X = df_encoded.drop('Attrition', axis=1)
    y = df_encoded['Attrition']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    sm = SMOTE(random_state=42)
    X_train_sm, y_train_sm = sm.fit_resample(X_train, y_train)

    return X_train_sm, X_test, y_train_sm, y_test
