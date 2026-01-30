from fastapi import FastAPI
import joblib
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ml.preprocessing import limpar_dados_triagem, preparar_para_modelo

app = FastAPI(title="SmartFlow Health Analytics API")

# Carregar o modelo treinado ao iniciar a API
MODEL_PATH = "../src/models/model.pkl"
modelo = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "API de Triagem Hospitalar está online!"}

@app.post("/predict")
def predict(paciente: dict):
    # Transformar os dados recebidos em um DataFrame
    df_paciente = pd.DataFrame([paciente])
    
    # Limpar e preparar os dados para o modelo
    df_limpo = limpar_dados_triagem(df_paciente)
    X = preparar_para_modelo(df_limpo)
    
    # Fazer a previsão
    predicao = modelo.predict(X)[0]
    
    return {
        "triage_level": int(predicao),
        "status": "sucesso"
    }