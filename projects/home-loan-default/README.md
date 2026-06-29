# Home Loan Default Prediction

Binary classification project using a Keras ANN to predict whether a borrower will default on a home equity loan. Trained on the HMEQ dataset with an 80/20 class imbalance.

---

## Dataset

**Source:** [HMEQ Dataset — Kaggle](https://www.kaggle.com/datasets/ajay1735/hmeq-data)
**Records:** 5,960 | **Features:** 12 | **Target:** BAD (0 = Repaid, 1 = Defaulted)

| Column | Description |
|--------|-------------|
| `BAD` | Target — 1 = defaulted or seriously delinquent, 0 = repaid |
| `LOAN` | Amount of the loan request |
| `MORTDUE` | Amount due on existing mortgage |
| `VALUE` | Current appraised value of the property |
| `REASON` | Loan purpose — HomeImp or DebtCon |
| `JOB` | Applicant occupational category |
| `YOJ` | Years at current job |
| `DEROG` | Number of major derogatory reports |
| `DELINQ` | Number of delinquent credit lines |
| `CLAGE` | Age of oldest credit line in months |
| `NINQ` | Number of recent credit inquiries |
| `CLNO` | Total number of existing credit lines |
| `DEBTINC` | Debt-to-income ratio |

---

## Approach

- Exploratory data analysis: class distribution, feature distributions, correlation heatmap, categorical breakdowns
- Missing values imputed using median (numeric) and most frequent value (categorical) — no rows dropped
- Stratified 70/15/15 train/val/test split
- Class weights computed from training data to handle 80/20 imbalance
- Logistic Regression baseline trained first for comparison
- ANN built with Keras: two Dense layers with Dropout, sigmoid output, EarlyStopping on val AUC
- Optimal classification threshold selected using Youden's J statistic

---

## Results

| Model | Accuracy | AUC | Recall (Default) |
|-------|----------|-----|------------------|
| Logistic Regression | ~0.77 | 0.7707 | 0.64 |
| ANN | ~0.77 | 0.7946 | 0.70 |

The ANN outperforms the baseline on AUC and recall for the minority class. False negatives were reduced from 64 to 53 using the optimal threshold.

---

## Limitations

- Small dataset (5,960 rows) limits model generalization
- DEBTINC had ~21% missing values — highest risk imputation
- Results are solid but not production-ready without more data and tuning

---

## Tools

Python, Keras, TensorFlow, scikit-learn, pandas, NumPy, matplotlib, seaborn

---

## How to Run

```bash
git clone https://github.com/NewManRising/the-builder-forge
cd home-loan-default
pip install -r requirements.txt
```

Download the dataset from the Kaggle link above and place it in `data/raw/`. Open and run `notebooks/home_loan.ipynb`.

---

## Folder Structure

```text
home-loan-default/
│
├── data/
│   ├── raw/
│   │   └── hmeq.csv
│   └── processed/
│
├── notebooks/
│   └── home_loan.ipynb
│
├── outputs/
│   ├── figures/
│   └── reports/
│       └── home_loan_report.txt
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Future Improvements

- Experiment with SMOTE for oversampling comparison
- Hyperparameter tuning on ANN architecture
- Add SHAP values for model explainability
- Deploy as a Streamlit app with CSV upload and risk scoring