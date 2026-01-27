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

## ⚙️ Metodologia

### 1️⃣ Pré-processamento dos Dados
- Análise exploratória do dataset (EDA);
- Tratamento de valores ausentes;
- Codificação de variáveis categóricas (*encoding*);
- Separação entre variáveis independentes (features) e variável alvo (target);
- Divisão em conjuntos de treino e teste.

---

### 2️⃣ Modelagem
Foram avaliados algoritmos de classificação, com foco inicial em:

- **Árvore de Decisão**
  - Alta interpretabilidade;
  - Fácil visualização das regras de decisão.

- **Random Forest**
  - Melhor desempenho em dados tabulares;
  - Redução de overfitting;
  - Capacidade de identificar a importância das variáveis.

Esses modelos foram escolhidos por equilibrar **performance e interpretabilidade**, fator essencial em aplicações na área da saúde.

---

### 3️⃣ Avaliação dos Modelos
Os modelos são avaliados utilizando as seguintes métricas:

- **Acurácia**
- **Precisão**
- **Recall (Sensibilidade)** — métrica prioritária para classes graves
- **F1-Score**
- **Matriz de Confusão**

📌 **Justificativa do Recall:**  
Em sistemas de triagem hospitalar, é fundamental minimizar a chance de que casos graves sejam classificados como não urgentes.

---

## 🧪 Tecnologias Utilizadas
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 📁 Estrutura do Projeto
