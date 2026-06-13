import joblib
import pandas as pd
from settings import settings
from fastapi import FastAPI, HTTPException
from schemas import Employee, PredictionResponse


app = FastAPI()
model = joblib.load(settings.model_path)


@app.get("/")
def home():
    return {"message": "Welcome to the Employee Attrition API"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict_attrition(employee: Employee) -> PredictionResponse:
    try:
        df = pd.DataFrame([employee.model_dump()])
        df = pd.get_dummies(df)

        # Align columns to match training data
        model_features = model.feature_names_in_
        df = df.reindex(columns=model_features, fill_value=0)

        prob = model.predict_proba(df)[0][1]

        if prob < 0.2:
            risk_zone = 'Safe Zone (Green)'
        elif prob < 0.5:
            risk_zone = "Low Risk (Yellow)"
        elif prob < 0.8:
            risk_zone = "Medium Risk (Orange)"
        else:
            risk_zone = "High Risk (Red)"

        return PredictionResponse(Probability=round(prob, 2), Risk_Zone=risk_zone)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
