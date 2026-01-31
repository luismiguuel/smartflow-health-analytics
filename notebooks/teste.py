import pandas as pd
import joblib
import os
import sys

# Garante que o Python encontre o seu módulo de pré-processamento
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ml.preprocessing import limpar_dados_triagem, preparar_para_modelo

def inferencia_pontual():
    # 1. Parâmetros de entrada
    entrada = {
        "age": 28.0,
        "heart_rate": 72.0,
        "systolic_blood_pressure": 120.0,
        "oxygen_saturation": 98.0,
        "body_temperature": 36.6,
        "pain_level": 2,
        "chronic_disease_count": 0,
        "previous_er_visits": 0,
        "arrival_mode": "walk_in"
    }

    # 2. Carregar o modelo de Regressão Logística
    MODEL_PATH = "../src/models/LogisticRegression.pkl"
    
    if os.path.exists(MODEL_PATH):
        modelo = joblib.load(MODEL_PATH)
        
        # 3. Transformar em DataFrame e Processar
        df_paciente = pd.DataFrame([entrada])
        df_limpo = limpar_dados_triagem(df_paciente)
        X_input = preparar_para_modelo(df_limpo)
        
        # 4. Predição
        predicao = modelo.predict(X_input)[0]
        probabilidades = modelo.predict_proba(X_input)[0]
        
        # 5. Exibir Resultado
        niveis = {0: "Baixo", 1: "Médio", 2: "Alto", 3: "Crítico"}
        print(f"Resultado da Inferência (Logistic Regression):")
        print(f"Nível de Triagem: {predicao} ({niveis[predicao]})")
        print(f"Confiança: {probabilidades[predicao]*100:.2f}%")
    else:
        print("Modelo LogisticRegression.pkl não encontrado.")

if __name__ == "__main__":
    inferencia_pontual()