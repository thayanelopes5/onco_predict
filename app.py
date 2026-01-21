import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="OncoPredict",
    page_icon="🧬",
    layout="wide"
)

# ===============================
# ESTILO (CSS leve)
# ===============================
st.markdown(
    """
    <style>
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🧬 OncoPredict")
st.sidebar.caption("Plataforma de apoio à decisão em oncologia")

menu = st.sidebar.radio(
    "Navegação",
    ["Visão Geral", "Simulação", "Sobre"]
)

# ===============================
# TÍTULO PRINCIPAL
# ===============================
st.title("OncoPredict 🧬")
st.caption("Protótipo conceitual para medicina personalizada em oncologia")

# ===============================
# VISÃO GERAL
# ===============================
if menu == "Visão Geral":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="card">
            <h4>🎯 Objetivo</h4>
            Apoiar decisões clínicas integrando múltiplas variáveis
            além de protocolos fixos.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h4>🧠 Diferencial</h4>
            Análise personalizada considerando fatores clínicos,
            biológicos e contextuais.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
            <h4>🚀 Status</h4>
            Protótipo em desenvolvimento para submissão
            ao Programa Centelha.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.info("Este sistema ainda **não realiza recomendações clínicas reais**.")

# ===============================
# SIMULAÇÃO
# ===============================
elif menu == "Simulação":

    st.subheader("Simulação Conceitual de Tratamento")

    col1, col2 = st.columns(2)

    with col1:
        idade = st.slider("Idade do paciente", 0, 100, 50)
        estadio = st.selectbox(
            "Estágio do câncer",
            ["I", "II", "III", "IV"]
        )

    with col2:
        st.markdown(
            """
            <div class="card">
            <h4>📊 Parâmetros Selecionados</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.write(f"**Idade:** {idade} anos")
        st.write(f"**Estágio:** {estadio}")

    # Gráfico fictício
    x = np.linspace(0, 10, 50)
    y = np.random.rand(50)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Exemplo de saída do modelo (dados fictícios)")

    st.pyplot(fig)

# ===============================
# SOBRE
# ===============================
elif menu == "Sobre":

    st.markdown(
        """
        <div class="card">
        <h3>Sobre o OncoPredict</h3>

        O **OncoPredict** é um projeto em desenvolvimento com foco em:

        - Medicina personalizada
        - Apoio à decisão clínica
        - Integração de dados heterogêneos
        - Transparência e interpretabilidade

        <br>
        <strong>Submissão:</strong> Programa Centelha
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Protótipo funcional — em evolução contínua.")
