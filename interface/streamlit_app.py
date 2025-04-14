import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Charger modèle et scaler
model = load_model("../model/model.h5")
scaler = joblib.load("../model/scaler.pkl")

st.title("💹 Prédiction du prix de clôture Forex (LSTM)")
st.markdown("Prédiction basée sur les données d'hier : `Open`, `High`, `Low`, `Moy2W`, `MoyMonth`")

# Formulaire d’entrée utilisateur
open_ = st.number_input("Open", format="%.5f")
high = st.number_input("High", format="%.5f")
low = st.number_input("Low", format="%.5f")
moy2w = st.number_input("Moyenne sur 2 semaines", format="%.5f")
moymonth = st.number_input("Moyenne sur 1 mois", format="%.5f")

if st.button("🔮 Prédire le prix Close"):
    # Préparation des données
    input_data = np.array([[open_, high, low, moy2w, moymonth]])
    input_scaled = scaler.transform(np.hstack([input_data, np.zeros((1, 1))]))[:, :-1]  # scaler toutes les colonnes sauf 'Close'
    input_scaled = np.expand_dims(input_scaled, axis=0)  # (1, 1, 5)

    prediction = model.predict(input_scaled)
    predicted_close = scaler.inverse_transform(np.hstack([np.zeros((1, 5)), prediction]))[:, -1][0]

    st.success(f"💰 Prix de clôture prédit : **{predicted_close:.5f}**")
