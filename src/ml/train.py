import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from preprocessing import limpar_dados_triagem, preparar_para_modelo

def executar_treinamento():
    DATA_PATH = "../../data/raw/synthetic_medical_triage.csv"
    MODEL_SAVE_PATH = "../models/model.pkl"

    print("Iniciando o pipeline de treinamento...")

    # Crregar dados
    if not os.path.exists(DATA_PATH):
        print(f"Erro: Arquivo não encontrado em {DATA_PATH}")
        return

    df = pd.read_csv(DATA_PATH)

    # Pré-processamento
    print("Limpando e preparando os dados...")
    df_limpo = limpar_dados_triagem(df)
    
    # Separar X (características) e y (alvo)
    X = preparar_para_modelo(df_limpo)
    y = df['triage_level']

    # Treinar o modelo
    print("Treinando a Inteligência Artificial...")
    modelo = RandomForestClassifier(
        n_estimators=100, 
        max_depth=10, 
        random_state=42, 
        class_weight="balanced"
    )
    modelo.fit(X, y)

    # Salvar o modelo
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    joblib.dump(modelo, MODEL_SAVE_PATH)
    
    print(f"Sucesso! Modelo salvo em: {MODEL_SAVE_PATH}")

if __name__ == "__main__":
    executar_treinamento()