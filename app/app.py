# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from main import predict_close
## App Flask
app = FastAPI(title="Prédicteur Forex LSTM")

# Modèle d'entrée avec Pydantic
class ForexInput(BaseModel):
    Open: float
    High: float
    Low: float
    Moy2W: float
    MoyMonth: float

@app.get("/")
def root():
    return {"message": "API de prédiction du prix de clôture Forex 📈"}

@app.post("/predict")
def predict_price(data: ForexInput):
    result = predict_close(data.dict())
    return {"prediction_close": round(result, 5)}
