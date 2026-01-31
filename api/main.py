from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(
    title="SmartFlow Health Analytics API",
    description="API para predição de nível de triagem hospitalar (0 a 3)"
)

# --- CONFIGURAÇÕES E CARREGAMENTO ---
# Altere o nome do arquivo para o modelo que você deseja usar (ex: LogisticRegression.pkl)
MODEL_NAME = "LogisticRegression.pkl"
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "models", MODEL_NAME)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modelo não encontrado em: {MODEL_PATH}")

modelo = joblib.load(MODEL_PATH)

# --- ESQUEMA DE ENTRADA (Validação de Dados) ---
class Paciente(BaseModel):
    age: float
    heart_rate: float
    systolic_blood_pressure: float
    oxygen_saturation: float
    body_temperature: float
    pain_level: int
    chronic_disease_count: int
    previous_er_visits: int
    arrival_mode: str  # 'walk_in', 'wheelchair' ou 'ambulance'

# --- FUNÇÕES AUXILIARES DE TRATAMENTO ---
def realizar_feature_engineering_api(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replica exatamente as transformações feitas durante o treinamento.
    """
    # 1. One-Hot Encoding manual para garantir consistência de colunas
    modos = ['arrival_ambulance', 'arrival_walk_in', 'arrival_wheelchair']
    for modo in modos:
        categoria = modo.replace('arrival_', '')
        df[modo] = (df['arrival_mode'] == categoria).astype(int)
    
    # 2. Criar Feature Auxiliar (Gatilho Clínico)
    df['low_oxygen_alert'] = (df['oxygen_saturation'] < 92).astype(int)
    
    # 3. Remover a coluna original de texto
    df = df.drop(columns=['arrival_mode'])
    
    # Garantir a ordem das colunas igual ao X_train
    # A ordem deve ser: age, heart_rate, systolic_blood_pressure, oxygen_saturation, 
    # body_temperature, pain_level, chronic_disease_count, previous_er_visits, 
    # arrival_ambulance, arrival_walk_in, arrival_wheelchair, low_oxygen_alert
    ordem_colunas = [
        'age', 'heart_rate', 'systolic_blood_pressure', 'oxygen_saturation',
        'body_temperature', 'pain_level', 'chronic_disease_count', 
        'previous_er_visits', 'arrival_ambulance', 'arrival_walk_in', 
        'arrival_wheelchair', 'low_oxygen_alert'
    ]
    return df[ordem_colunas]

# --- ENDPOINTS ---
@app.get("/")
def home():
    return {
        "message": "API de Triagem Hospitalar Online",
        "modelo_ativo": MODEL_NAME,
        "documentacao": "/docs"
    }

@app.post("/predict")
def predict(paciente: Paciente):
    try:
        # 1. Converter entrada Pydantic para DataFrame
        df_entrada = pd.DataFrame([paciente.model_dump()])
        
        # 2. Processamento Interno (Sem dependências externas)
        X = realizar_feature_engineering_api(df_entrada)
        
        # 3. Predição
        predicao = modelo.predict(X)[0]
        probabilidades = [round(float(p), 4) for p in modelo.predict_proba(X)[0]]
        
        # 4. Mapeamento de labels (Opcional, para facilitar leitura)
        niveis = {0: "Baixo", 1: "Médio", 2: "Alto", 3: "Crítico"}
        
        return {
            "triage_level": int(predicao),
            "triage_label": niveis.get(int(predicao), "Desconhecido"),
            "confidence_scores": {
                "0": probabilidades[0],
                "1": probabilidades[1],
                "2": probabilidades[2],
                "3": probabilidades[3]
            },
            "status": "sucesso"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no processamento: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)