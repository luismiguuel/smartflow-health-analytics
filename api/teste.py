import pandas as pd
from main import realizar_feature_engineering_api, modelo, Paciente

def testar_inferencia_direta():
    # 1. Dados do paciente (Dicionário)
    dados_paciente = {
        "age": 72.0,
        "heart_rate": 115.0,
        "systolic_blood_pressure": 95.0,
        "oxygen_saturation": 89.0,
        "body_temperature": 38.8,
        "pain_level": 9,
        "chronic_disease_count": 3,
        "previous_er_visits": 1,
        "arrival_mode": "ambulance" # Note: use o padrão minúsculo definido na sua API
    }

    print("--- Iniciando Inferência Direta (Sem API) ---")

    try:
        # 2. Validar dados com o esquema Pydantic da API
        # Isso garante que o teste use as mesmas regras de validação da API
        paciente_validado = Paciente(**dados_paciente)
        
        # 3. Converter para DataFrame
        df_entrada = pd.DataFrame([paciente_validado.model_dump()])
        
        # 4. Chamar a função de tratamento que está no main.py
        X = realizar_feature_engineering_api(df_entrada)
        
        # 5. Fazer a predição usando o objeto 'modelo' carregado no main.py
        predicao = modelo.predict(X)[0]
        probabilidades = modelo.predict_proba(X)[0]
        
        # Mapeamento para exibição
        niveis = {0: "Baixo", 1: "Médio", 2: "Alto", 3: "Crítico"}
        
        print(f"\nResultado:")
        print(f"Nível Previsto: {predicao} ({niveis[predicao]})")
        print(f"Probabilidades: {probabilidades}")
        print(f"Status: Sucesso")

    except Exception as e:
        print(f"Erro durante a inferência: {e}")

if __name__ == "__main__":
    testar_inferencia_direta()