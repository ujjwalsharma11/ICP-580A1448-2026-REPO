from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting California house values using the trained Project 2 Random Forest model.",
    version="1.0.0"
)

MODEL_PATH = "house_price_model.joblib"
model = joblib.load(MODEL_PATH)


class HouseFeatures(BaseModel):
    MedInc: float = Field(..., description="Median income in the block")
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float
    RoomsPerHousehold: float
    BedroomsPerRoom: float


@app.get("/")
def root():
    return {
        "message": "House Price Prediction API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict")
def predict(features: HouseFeatures):
    data = np.array([[
        features.MedInc,
        features.HouseAge,
        features.AveRooms,
        features.AveBedrms,
        features.Population,
        features.AveOccup,
        features.Latitude,
        features.Longitude,
        features.RoomsPerHousehold,
        features.BedroomsPerRoom
    ]])

    prediction = float(model.predict(data)[0])

    return {
        "predicted_house_value": round(prediction, 4),
        "unit": "hundreds of thousands of USD"
    }
