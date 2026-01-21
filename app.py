import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Precognium",
    page_icon="🧬",
    layout="wide"
)

# ===============================
# ESTILO VISUAL
# ===============================
st.markdown(
    """
    <style>
        .card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 14px;
            box-shadow: 0 6px 14px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ===============================
# SIDEBAR
# ===============================
st.sidebar.title("🧬 Precognium")
st.sidebar.caption("Apoio à decisão clínica em oncologia")

menu = st.sidebar.radio(
    "Navegação",
    [
        "Visão Geral",
        "Perfil do Tumor",
        "Simulação de Tratamento",
        "Sobre"
    ]
)

# ===============================
# TÍTULO
# ===============================
st.title("Precognium 🧬")
st.caption("Plataforma conceitual para medicina personalizada em oncologia")

# ===============================
# VISÃO GERAL
# ===============================
if menu == "Visão Geral":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>🎯 Objetivo</h4>
        Integrar múltiplos parâmetros clínicos e biológicos
        para apoiar decisões terapêuticas.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🧬 Diferencial</h4>
        Considera subtipo tumoral, perfil molecular
        e características do paciente.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h4>🚀 Status</h4>
        Protótipo funcional para submissão
        ao Programa Centelha.
        </div>
        """, unsafe_allow_html=True)

    st.info("⚠️ Protótipo conceitual — não substitui decisão médica.")

# ===============================
# PERFIL DO TUMOR
# ===============================
elif menu == "Perfil do Tumor":

    st.subheader("🧬 Perfil Biológico do Tumor")

    col1, col2 = st.columns(2)

    with col1:
        tipo_cancer = st.selectbox(
            "Tipo de câncer",
            ["Mama", "Leucemia"]
        )

        estadio = st.selectbox(
            "Estágio clínico",
            ["I", "II", "III", "IV"]
        )

        subtipo_hr = st.selectbox(
            "Status hormonal (HR)",
            [
                "HR+ (Receptor hormonal positivo)",
                "HR- (Receptor hormonal negativo)",
                "Não aplicável"
            ]
        )

    with col2:
        st.markdown("""
        <div class="card">
        <h4>📋 Resumo do Perfil</h4>
        </div>
        """, unsafe_allow_html=True)

        st.write(f"**Câncer:** {tipo_cancer}")
        st.write(f"**Estágio:** {estadio}")
        st.write(f"**Status HR:** {subtipo_hr}")

# ===============================
# SIMULAÇÃO DE TRATAMENTO
# ===============================
elif menu == "Simulação de Tratamento":

    st.subheader("💊 Simulação Conceitual de Tratamento")

    col1, col2 = st.columns(2)

    with col1:
        idade = st.slider("Idade do paciente", 0, 100, 55)

        tipo_tratamento = st.multiselect(
            "Modalidades terapêuticas consideradas",
            [
                "Cirurgia",
                "Quimioterapia",
                "Radioterapia",
                "Terapia Hormonal",
                "Imunoterapia",
                "Terapia Alvo"
            ]
        )

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🧠 Interpretação do Modelo (fictícia)</h4>
        </div>
        """, unsafe_allow_html=True)

        st.write(f"**Idade:** {idade} anos")
        st.write(f"**Tratamentos considerados:**")
        for t in tipo_tratamento:
            st.write(f"- {t}")

    # Gráfico ilustrativo
    x = np.linspace(0, 10, 50)
    y = np.random.rand(50)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Resposta estimada ao tratamento (dados fictícios)")

    st.pyplot(fig)

    st.warning("Resultados exibidos são apenas ilustrativos.")

# ===============================
# SOBRE
# ===============================
elif menu == "Sobre":

    st.markdown("""
    <div class="card">
    <h3>Sobre o Projeto</h3>

    O <strong>OncoPredict</strong> busca apoiar decisões clínicas
    por meio da integração de:

    - Perfil molecular do tumor
    - Características do paciente
    - Modalidades terapêuticas
    - Evidências clínicas

    <br><br>
    Projeto em fase de prototipação — Programa Centelha.
    </div>
    """, unsafe_allow_html=True)

    st.success("Interface e lógica em evolução contínua.")
