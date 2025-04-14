# Étape 1 : image de base
FROM python:3.12-slim

# Étape 2 : définir le répertoire de travail
WORKDIR /app

# Étape 3 : copier les fichiers requis
COPY requirements.txt .
COPY app/ app/
COPY model/ model/
COPY data/ data/

# Étape 4 : installer les dépendances
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Étape 5 : exposer les ports pour FastAPI (8000) et Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Étape 6 : lancer Streamlit et FastAPI simultanément
CMD ["sh", "-c", "uvicorn app.app:app --host 0.0.0.0 --port 8000 & streamlit run app/streamlit_app.py --server.port 8501"]
