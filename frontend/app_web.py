import streamlit as st
import requests

st.set_page_config(page_title="SmartFlow - Triagem Inteligente", page_icon="🏥", layout="wide")

st.title("🏥 SmartFlow: Triagem Hospitalar")
st.markdown("Preencha os dados do paciente para obter a classificação de risco via IA.")

# Criando o formulário na interface
with st.form("form_triagem"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sinais Vitais")
        age = st.number_input("Idade", min_value=0, max_value=120, value=30)
        heart_rate = st.number_input("Frequência Cardíaca (bpm)", value=80)
        systolic_bp = st.number_input("Pressão Sistólica (mmHg)", value=120)
        oxygen = st.number_input("Saturação de Oxigênio (%)", value=98)
        temp = st.number_input("Temperatura (°C)", value=36.5, format="%.1f")
    
    with col2:
        st.subheader("Histórico e Chegada")
        pain = st.slider("Nível de Dor (0-10)", 0, 10, 5)
        chronic = st.number_input("Doenças Crônicas", 0, 10, 0)
        er_visits = st.number_input("Visitas anteriores ao ER", 0, 100, 0)
        # O selectbox agora usa os valores exatos que a API espera
        arrival = st.selectbox("Modo de Chegada", ["walk_in", "ambulance", "wheelchair"], 
                               format_func=lambda x: x.replace('_', ' ').title())

    submit = st.form_submit_button("Classificar Risco")

if submit:
    # Organiza os dados para enviar para a API
    dados_paciente = {
        "age": float(age),
        "heart_rate": float(heart_rate),
        "systolic_blood_pressure": float(systolic_bp),
        "oxygen_saturation": float(oxygen),
        "body_temperature": float(temp),
        "pain_level": int(pain),
        "chronic_disease_count": int(chronic),
        "previous_er_visits": int(er_visits),
        "arrival_mode": arrival
    }

    try:
        # Faz a chamada para a API
        response = requests.post("http://127.0.0.1:8000/predict", json=dados_paciente)
        
        if response.status_code == 200:
            res = response.json()
            nivel = res["triage_level"]
            label = res["triage_label"]
            confs = res["confidence_scores"]

            # Estilização baseada no nível de triagem (Protocolo Manchester Adaptado)
            cores = {0: "blue", 1: "green", 2: "#FFA500", 3: "red"}
            cor = cores.get(nivel, "gray")

            st.divider()
            
            # Layout de Resultado
            c1, c2 = st.columns([1, 1])
            
            with c1:
                st.subheader("Resultado da IA")
                st.markdown(f"### Classificação: <span style='color:{cor}; font-weight:bold;'>{label.upper()}</span>", unsafe_allow_html=True)
                st.metric("Nível de Prioridade", nivel)
            
            with c2:
                st.subheader("Grau de Confiança")
                # Exibe as probabilidades em barras para facilitar a leitura
                for n, prob in confs.items():
                    texto_nivel = { "0": "Baixo", "1": "Médio", "2": "Alto", "3": "Crítico" }
                    # p_num = float(prob) # Caso você use a Opção B de strings no back, converta aqui
                    st.write(f"{texto_nivel[n]}")
                    st.progress(prob)
                    st.caption(f"{prob * 100:.2f}% de probabilidade")

        else:
            st.error(f"Erro na API: {response.text}")
        
    except Exception as e:
        st.error(f"Não foi possível conectar à API. Verifique se o servidor FastAPI está rodando em http://127.0.0.1:8000. Erro: {e}")