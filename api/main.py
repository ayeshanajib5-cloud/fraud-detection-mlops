from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

MODEL_PATH = os.getenv("MODEL_PATH", "models/fraud_model.pkl")
EXPECTED_FEATURES = 30

app = FastAPI(title="Fraud Detection API")
prediction_counter = Counter("prediction_requests_total", "Total prediction requests")
fraud_counter = Counter("fraud_predictions_total", "Total fraud predictions")

model = joblib.load(MODEL_PATH)

class Transaction(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post("/predict")
def predict(transaction: Transaction):
    if len(transaction.features) != EXPECTED_FEATURES:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {EXPECTED_FEATURES} features, but got {len(transaction.features)}"
        )

    data = pd.DataFrame([transaction.features])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    prediction_counter.inc()

    if prediction == 1:
        fraud_counter.inc()

    return {
        "prediction": "fraud" if prediction == 1 else "not fraud",
        "fraud_probability": round(float(probability), 4)
    }