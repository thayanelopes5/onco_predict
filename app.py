import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -------------------------------
st.set_page_config(
    page_title="OncoPredict",
    page_icon="🧬",
    layout="wide"
)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("🧬 OncoPredict")
st.sidebar.markdown("Plataforma de apoio à decisão em oncologia")

menu = st.sidebar.radio(
    "Navegação",
    [
        "Visão Geral",
        "Simulação de Tratamento",
        "Sobre o Projeto"
    ]
)

# -------------------------------
# CONTEÚDO PRINCIPAL
# -------------------------------
st.title("OncoPredict 🧬")

if menu == "Visão Geral":
    st.subheader("Visão Geral do Protótipo")

    st.markdown(
        """
        Este é um **protótipo inicial** da plataforma **OncoPredict**, 
        desenvolvida para apoiar decisões clínicas em oncologia.

        🔹 Objetivo: integrar múltiplas variáveis clínicas, biológicas e contextuais  
        🔹 Foco inicial: **câncer de mama** e **leucemias**  
        🔹 Evolução futura: incorporação de estudos clínicos e IA preditiva
        """
    )

    st.info("Este protótipo ainda não realiza recomendações clínicas reais.")

elif menu == "Simulação de Tratamento":
    st.subheader("Simulação (Protótipo Conceitual)")

    idade = st.slider("Idade do paciente", 0, 100, 50)
    estadio = st.selectbox(
        "Estágio do câncer",
        ["I", "II", "III", "IV"]
    )

    st.markdown("### Parâmetros selecionados")
    st.write(f"- Idade: **{idade} anos**")
    st.write(f"- Estágio: **{estadio}**")

    # Gráfico fictício apenas para visualização
    x = np.linspace(0, 10, 50)
    y = np.random.rand(50)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Exemplo de saída do modelo (fictícia)")

    st.pyplot(fig)

elif menu == "Sobre o Projeto":
    st.subheader("Sobre o OncoPredict")

    st.markdown(
        """
        **OncoPredict** é um projeto em desenvolvimento com foco em:

        - Medicina personalizada
        - Integração de múltiplas variáveis
        - Apoio à decisão clínica
        - Transparência e interpretabilidade

        🚀 Projeto submetido ao **Programa Centelha**
        """
    )

    st.success("Este projeto está em fase de prototipação.")
