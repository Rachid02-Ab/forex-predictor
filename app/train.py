import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
import joblib

# Charger les données
df = pd.read_excel("../data/dataForex.xlsx")

# Garder les colonnes nécessaires
df = df[['Open', 'High', 'Low', 'Moy2W', 'MoyMonth', 'J (Close)']]
df.dropna(inplace=True)

# Normalisation
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

# Séparer les features (sans Close) et target (Close du jour suivant)
X = []
y = []

for i in range(len(scaled) - 1):
    X.append(scaled[i, :-1])      # Données du jour i (sans Close)
    y.append(scaled[i + 1, -1])   # Close du jour suivant (target)

X = np.array(X)                   # Shape: (samples, features)
y = np.array(y)                   # Shape: (samples,)

# Reshape pour LSTM: (samples, timesteps=1, features)
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Construire le modèle LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=False, input_shape=(1, X.shape[2])))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

# Entraînement
model.fit(X, y, epochs=20, batch_size=16, verbose=1, callbacks=[EarlyStopping(patience=3)])

# Sauvegarde du modèle
os.makedirs("model", exist_ok=True)
model.save("../model/model.h5")

# Sauvegarde du scaler
joblib.dump(scaler, "../model/scaler.pkl")

print("✅ Modèle entraîné et sauvegardé dans le dossier /model")
