
## What This Project Is
I converted my UT Dallas/Full Stack bootcamp notebook into an API. I separated out sections into their own scripts to make it modular.

Four files were made to create and evaluate the model: load.py, features.py, train.py, and evaluate.py. 

I compared three models (logistic regression, random forest, and gradient boosting) and chose the best one based on ROC-AUC score. Gradient Boosting was the winner with ROC-AUC of 0.7669.

I used the IBM HR Attrition data to retrain the models instead of the original dataset that was used in my bootcamp notebook. You can download the data here:

Download the IBM HR Analytics dataset from Kaggle and place it in `data/ibm_hr_attrition.csv`:
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

## Project Structure

```text
employee-attrition/
├── api/
│   ├── main.py          # FastAPI app and routes
│   ├── schemas.py       # Pydantic input/output models
│   └── settings.py      # Configuration and model path
├── data/
│   └── ibm_hr_attrition.csv  # Download from Kaggle 
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── gradient_boosting.pkl  # Best performer (Used by API)
├── notebooks/
│   ├── eda.ipynb        # Exploratory data analysis
│   └── figures/         # Saved plots and visualizations
├── src/
│   ├── load.py          # Data loading and deduplication
│   ├── features.py      # Encoding, train/test split, SMOTE
│   ├── train.py         # Model training and saving
│   └── evaluate.py      # Classification reports and ROC-AUC
├── requirements.txt
└── README.md
```


## Installation & Set Up
```bash

# Clone the repo
git clone https://github.com/NewManRising/the-builder-forge.git
cd the-builder-forge/projects/employee-attrition

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download the IBM HR Analytics dataset from Kaggle and place it at:
 
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

# Train the models
python -m src.train

# Run the API

uvicorn api.main:app --reload
```

## API Usage
```text
Endpoint: POST /predict
Example request:

{
  "Age": 32,
  "BusinessTravel": "Travel_Rarely",
  "DailyRate": 800,
  "Department": "Sales",
  "DistanceFromHome": 10,
  "Education": 3,
  "EducationField": "Life Sciences",
  "EnvironmentSatisfaction": 2,
  "Gender": "Male",
  "HourlyRate": 50,
  "JobInvolvement": 2,
  "JobLevel": 1,
  "JobRole": "Sales Representative",
  "JobSatisfaction": 1,
  "MaritalStatus": "Single",
  "MonthlyIncome": 2500,
  "MonthlyRate": 10000,
  "NumCompaniesWorked": 3,
  "OverTime": "Yes",
  "PercentSalaryHike": 11,
  "PerformanceRating": 3,
  "RelationshipSatisfaction": 2,
  "StockOptionLevel": 0,
  "TotalWorkingYears": 5,
  "TrainingTimesLastYear": 2,
  "WorkLifeBalance": 1,
  "YearsAtCompany": 2,
  "YearsInCurrentRole": 1,
  "YearsSinceLastPromotion": 1,
  "YearsWithCurrManager": 1
}
```
## Example Response
```text
{
  "attrition_probability": 0.98,
  "risk_zone": "High Risk"
}
```

You can also explore all endpoints interactively at http://127.0.0.1:8000/docs after starting the server.