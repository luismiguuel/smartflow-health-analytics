# 🏥 SmartFlow: Health Analytics & Triagem Inteligente

O **SmartFlow** é uma solução de suporte à decisão clínica que utiliza Machine Learning para automatizar a classificação de risco (triagem) em unidades de pronto-socorro. Através da análise de sinais vitais e histórico clínico, o sistema classifica o paciente em quatro níveis de urgência (0 a 3), priorizando casos críticos (como hipóxia e instabilidade hemodinâmica) para garantir agilidade no atendimento e segurança assistencial.

O projeto conta com um modelo de **Regressão Logística** de alta performance, uma **API FastAPI** para inferência em tempo real e uma interface amigável desenvolvida em **Streamlit**.

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar o ambiente e executar a aplicação.

### 1. Configuração do Ambiente (Virtualenv)

Na raiz do projeto, você deve criar e ativar o ambiente virtual para garantir que as dependências não conflitem com seu sistema.

**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate