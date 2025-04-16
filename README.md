# 🧠 Forex Price Predictor with LSTM

Ce projet utilise un modèle de Deep Learning (LSTM) pour prédire le **prix de clôture** du Forex à partir des données historiques (Open, High, Low, moyennes mobiles, etc.).


## 🧪 Fonctionnalités

- 📊 **Entraînement LSTM** sur 30 jours d'historique de données multivariées.
- 🔮 **Prédiction du prix de clôture** du jour suivant.
- ⚙️ **API REST** (FastAPI) pour intégrer le modèle n'importe où.
- 💻 **Interface Streamlit** interactive pour tester les prédictions.


###  Cloner le projet

-- git clone https://github.com/Rachid02-Ab/forex-predictor.git
-- cd FINANCIAL-PRICE-PREDICTOR

### Installer les dépendances

-- pip install -r requirements.txt

### 🧠 Technologies utilisées
Python 3.12
TensorFlow / Keras
LSTM
FastAPI
Streamlit
Pandas, NumPy, Scikit-learn

## ⚙️ CI/CD avec GitHub Actions

Ce projet inclut une **pipeline CI/CD** automatisée grâce à **GitHub Actions**.  
Elle se déclenche à chaque `push` ou `pull request` sur la branche `main`.

### 🔁 Étapes de la pipeline :

- 🔄 **Checkout** du dépôt Git.  
- 🐍 **Installation de Python 3.12.**  
- 📦 **Installation des dépendances** du projet.  
- 🧠 **Exécution automatique de l'entraînement du modèle** via `train.py`.  
- ✅ **Vérification de la création du modèle** (`model.h5`) et du scaler (`scaler.pkl`).  
- 🚀 **Upload** du modèle entraîné en tant qu’artefact GitHub *(optionnel)*.

