import pandas as pd
from sklearn.preprocessing import StandardScaler

def limpar_dados_triagem(df):
    dados = df.copy()

    modos = ['Ambulance', 'Walk-in', 'Wheelchair']
    for modo in modos:
        col_name = f'arrival_{modo}'
        dados[col_name] = (dados['arrival_mode'] == modo).astype(int)
    
    # Remover a coluna original de texto
    dados.drop('arrival_mode', axis=1, inplace=True)

    # Criar alerta de oxigenação
    dados['low_oxygen_alert'] = (dados['oxygen_saturation'] < 92).astype(int)

    # Lista das colunas numéricas que precisam de escala
    numeric_cols = ['age', 'heart_rate', 'systolic_blood_pressure', 
                    'oxygen_saturation', 'body_temperature', 'pain_level', 
                    'chronic_disease_count', 'previous_er_visits']

    return dados

def preparar_para_modelo(df):
    # Definimos a ordem exata que o modelo viu no treino
    colunas_esperadas = [
        'age', 'heart_rate', 'systolic_blood_pressure', 'oxygen_saturation',
        'body_temperature', 'pain_level', 'chronic_disease_count', 
        'previous_er_visits', 'arrival_Ambulance', 'arrival_Walk-in', 
        'arrival_Wheelchair', 'low_oxygen_alert'
    ]
    
    return df[colunas_esperadas]