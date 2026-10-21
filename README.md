# Projeto_12_Previs-o_do_tempo
# 🌤️ Dashboard de Previsão do Tempo

Aplicação web interativa desenvolvida em Python para consulta de previsão do tempo para os próximos 7 dias em diferentes cidades do mundo.

---

## 📌 Sobre o Projeto

O objetivo deste projeto é fornecer uma interface simples e intuitiva para visualizar a temperatura média semanal. Ao selecionar uma cidade na barra lateral, o aplicativo obtém as coordenadas geográficas (latitude e longitude), realiza a busca dos dados meteorológicos e exibe um resumo diário acompanhado de ícones dinâmicos de clima.

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit** (para criação do dashboard interativo)
* **Pandas** (para manipulação e iteração dos dados de clima)

---

## ⚙️ Funcionalidades

- **Seleção de Cidades:** Escolha de localidades via menu lateral (`st.sidebar`), cobrindo cidades brasileiras e internacionais.
- **Integração Modular:** Separação entre a interface e a busca de dados na API (`dados_api.py`).
- **Cards Diários:** Exibição organizada por container para cada um dos 7 dias da semana.
- **Métricas Personalizadas:** Exibição limpa da data e da temperatura média.
- **Feedback Visual Dinâmico:** Alteração do ícone (frio, fresco, agradável, quente) conforme a faixa de temperatura prevista.

---

## 🚀 Como Executar o Projeto

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
