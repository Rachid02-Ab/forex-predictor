# main.py
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Charger le modèle et le scaler  a travers le chemin relatif
model = load_model("../model/model.h5")
scaler = joblib.load("../model/scaler.pkl")

# Fonction de prédiction
def predict_close(input_data: dict) -> float:
    """
    Prend les features d’un jour (Open, High, Low, Moy2W, MoyMonth)
    et retourne le Close prédit.
    """
    # Ordonner les features comme à l'entraînement
    features = ['Open', 'High', 'Low', 'Moy2W', 'MoyMonth']
    data = np.array([[input_data[feat] for feat in features]])

    # On recrée une ligne complète avec 0 en dernière colonne pour le Close (temporairement)
    fake_full_row = np.hstack([data, np.zeros((1, 1))])

    # Appliquer le même scaler
    scaled = scaler.transform(fake_full_row)[:, :-1]  # garder seulement les features

    # Reshape pour LSTM: (samples=1, timesteps=1, features=5)
    X_input = scaled.reshape((1, 1, scaled.shape[1]))

    # Prédiction
    y_pred_scaled = model.predict(X_input)
    
    # On recrée une ligne complète avec les features et la prédiction pour l'inverser avec scaler
    full_scaled = np.hstack([scaled, y_pred_scaled])
    y_pred = scaler.inverse_transform(full_scaled)[0, -1]  # récupérer le Close prédicté

    return float(y_pred)
