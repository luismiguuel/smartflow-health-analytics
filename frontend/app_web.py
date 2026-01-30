import streamlit as st
import requests

st.set_page_config(page_title="SmartFlow - Triagem Inteligente", page_icon="🏥")

st.title("🏥SmartFlow: Triagem Hospitalar")
st.markdown("Preencha os dados do paciente para obter a classificação de risco via IA.")

# Criando o formulário na interface
with st.form("form_triagem"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Idade", min_value=0, max_value=120, value=30)
        heart_rate = st.number_input("Frequência Cardíaca (bpm)", value=80)
        systolic_bp = st.number_input("Pressão Sistólica", value=120)
        oxygen = st.number_input("Saturação de Oxigênio (%)", value=98)
    
    with col2:
        temp = st.number_input("Temperatura (°C)", value=36.5)
        pain = st.slider("Nível de Dor (0-10)", 0, 10, 5)
        chronic = st.number_input("Doenças Crônicas", 0, 10, 0)
        arrival = st.selectbox("Modo de Chegada", ["Walk-in", "Ambulance", "Wheelchair"])

    submit = st.form_submit_button("Classificar Risco")

if submit:
    # Organiza os dados para enviar para a API
    dados_paciente = {
        "age": age,
        "heart_rate": heart_rate,
        "systolic_blood_pressure": systolic_bp,
        "oxygen_saturation": oxygen,
        "body_temperature": temp,
        "pain_level": pain,
        "chronic_disease_count": chronic,
        "previous_er_visits": 0, # Valor padrão
        "arrival_mode": arrival
    }

    # Faz a chamada para a API
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=dados_paciente)
        resultado = response.json()
        nivel = resultado["triage_level"]

        # Define cores baseadas no nível
        cores = {0: "blue", 1: "green", 2: "orange", 3: "red"}
        textos = {0: "Nível 0: Não Urgente", 1: "Nível 1: Pouco Urgente", 2: "Nível 2: Urgente", 3: "Nível 3: EMERGÊNCIA"}

        st.subheader(f"Resultado da IA:")
        st.write(f"### :{cores[nivel]}[{textos[nivel]}]")
        
    except Exception as e:
        st.error("Erro: A API está rodada? Certifique-se de que o uvicorn está ativo.")