import joblib
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt

from src.train import train_models
from sklearn.metrics import classification_report, roc_auc_score

plt.style.use("seaborn-v0_8")


MODELS_PATH = Path(__file__).resolve().parent.parent / "models"


def evaluate_models():
    X_test, y_test = train_models()

    model_names = ['Logistic_Regression', 'Random_Forest', 'Gradient_Boosting']

    for name in model_names:
        print(f"Evaluating {name}:")
        model = joblib.load(MODELS_PATH / f"{name}.pkl")
        pred = model.predict(X_test)
        prob = model.predict_proba(X_test)[:, 1]

        report = classification_report(y_test, pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose()

        plt.figure(figsize=(8, 4))
        sns.heatmap(pd.DataFrame(
            report_df).iloc[:-1, :-1].astype(float), fmt='.2f', annot=True, cmap='viridis')

        plt.title(f'Classification Report For {name}')
        plt.tight_layout()
        plt.savefig(
            f'notebooks/figures/{name}_report.png', dpi=300, bbox_inches='tight')
        plt.close()

        auc = roc_auc_score(y_test, prob)
        print(f'{name} ROC_AUC: {auc:.4f}')


if __name__ == "__main__":
    evaluate_models()
