import joblib
from pathlib import Path

from src.features import prepare_features

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier


MODELS_PATH = Path(__file__).resolve().parent.parent / "models"


def train_models():
    X_train, X_test, y_train, y_test = prepare_features()

    models = {
        'Logistic_Regression': Pipeline([
            ('scaler', StandardScaler()),
            ('model', LogisticRegression(max_iter=1000, random_state=42))
        ]),
        'Random_Forest': RandomForestClassifier(random_state=42),
        'Gradient_Boosting': GradientBoostingClassifier(random_state=42)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        joblib.dump(model, MODELS_PATH / f"{name}.pkl")

    return X_test, y_test


if __name__ == "__main__":
    train_models()
