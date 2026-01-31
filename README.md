# 🏥 Sistema Inteligente de Triagem Hospitalar com IA.

## 📌 Visão Geral
Este projeto tem como objetivo desenvolver um **sistema de otimização de triagem hospitalar** utilizando **Inteligência Artificial**, capaz de classificar automaticamente o **nível de urgência de pacientes** com base em dados clínicos e sinais vitais.

A proposta visa **auxiliar equipes hospitalares** no processo de admissão, melhorando o fluxo de atendimento, reduzindo o tempo de espera e evitando complicações causadas por atrasos no atendimento de casos críticos.

---

## 🎯 Objetivo
Classificar de forma **rápida, segura e eficiente** o nível de urgência de pacientes, com foco em:
- Melhorar a organização e alocação de recursos hospitalares;
- Reduzir filas e tempo de espera;
- Priorizar corretamente casos graves;
- Apoiar a tomada de decisão clínica, sem substituir o profissional de saúde.

---

## 🧠 Contexto do Projeto
O projeto está inserido no eixo temático de **Saúde e Bem-Estar**, explorando o uso responsável da Inteligência Artificial como ferramenta de apoio à área da saúde, respeitando princípios éticos e de interpretabilidade dos modelos.

---

## 📊 Dataset
- **Nome:** Synthetic Medical Triage Priority Dataset  
- **Fonte:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/emirhanakku/synthetic-medical-triage-priority-dataset  
- **Tipo:** Dataset sintético (não contém dados reais de pacientes)

### 📌 Características do dataset
- Dados simulados de triagem médica;
- Variáveis relacionadas a sinais vitais e condições clínicas;
- Coluna alvo representando o **nível de prioridade/urgência**;
- Dataset adequado para problemas de **classificação supervisionada**;
- Presença de possível **desbalanceamento de classes**, refletindo cenários reais de triagem.

> O uso de dados sintéticos elimina riscos de privacidade e torna o projeto adequado para fins acadêmicos e experimentais.

---


## 🧪 Tecnologias Utilizadas
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 📁 Como rodar
Para configurar o ambiente e rodar o projeto, comece criando um ambiente virtual na raiz do diretório com o comando python -m venv venv, ative-o utilizando .\venv\Scripts\activate no Windows ou source venv/bin/activate no Linux/macOS e instale as dependências necessárias através de pip install -r requirements.txt. Com o ambiente preparado, abra dois terminais distintos: no primeiro, acesse a pasta api e inicie o servidor com uvicorn main:app --reload para disponibilizar os serviços de inferência; no segundo, acesse a pasta frontend e execute streamlit run app_web.py para abrir a interface gráfica no seu navegador.

---