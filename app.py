# =============================================================================
# SISTEMA DE PREDIÇÃO DE TRATAMENTO ONCOLÓGICO
# MVP - Programa Centelha (Fase 2)
# Interface: Streamlit
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="IA Oncológica – Predição de Tratamento",
    layout="wide"
)

st.title("🧬 Sistema de Predição de Tratamento Oncológico")
st.caption("Protótipo de IA • Programa Centelha – Fase 2")
st.divider()

# -----------------------------------------------------------------------------
# GERAR DADOS SIMULADOS
# -----------------------------------------------------------------------------
@st.cache_data
def gerar_dados():
    np.random.seed(42)
    n = 1000

    dados = {
        'idade': np.random.normal(58, 12, n).astype(int),
        'sexo': np.random.choice(['F', 'M'], n, p=[0.99, 0.01]),
        'historico_familiar': np.random.choice([0, 1], n, p=[0.7, 0.3]),
        'estagio': np.random.choice([1, 2, 3, 4], n, p=[0.15, 0.40, 0.30, 0.15]),
        'tipo_tumor': np.random.choice(
            ['HR+', 'HER2+', 'Triplo_Negativo'], n, p=[0.7, 0.2, 0.1]
        ),
        'metastase': np.random.choice([0, 1], n, p=[0.65, 0.35]),
        'tamanho_tumor_cm': np.random.uniform(0.5, 8.0, n).round(1),
    }

    df = pd.DataFrame(dados)
    df.loc[df['estagio'] == 4, 'metastase'] = 1
    df.loc[df['estagio'] == 1, 'metastase'] = 0
    df['idade'] = df['idade'].clip(25, 85)

    return df

df = gerar_dados()

# -----------------------------------------------------------------------------
# FUNÇÕES DE NEGÓCIO
# -----------------------------------------------------------------------------
def atribuir_tratamento(estagio, tipo):
    if estagio == 1:
        return "Cirurgia + Hormonioterapia" if tipo == "HR+" else "Cirurgia + Imunoterapia"
    if estagio == 2:
        return "Quimioterapia + Cirurgia"
    if estagio == 3:
        return "Quimioterapia + Radioterapia"
    return "Quimioterapia Sistêmica"

def calcular_resultado(row):
    prob = 0.75
    if row['estagio'] >= 3:
        prob -= 0.2
    if row['metastase'] == 1:
        prob -= 0.2
    if row['idade'] > 70:
        prob -= 0.1
    return 1 if np.random.rand() < max(0.1, min(prob, 0.95)) else 0

df['resultado'] = df.apply(calcular_resultado, axis=1)

# -----------------------------------------------------------------------------
# TREINAR MODELO
# -----------------------------------------------------------------------------
df_modelo = df.copy()
df_modelo['sexo'] = df_modelo['sexo'].map({'F': 0, 'M': 1})
df_modelo['tipo_tumor'] = df_modelo['tipo_tumor'].map({
    'HR+': 0, 'HER2+': 1, 'Triplo_Negativo': 2
})

features = [
    'idade', 'sexo', 'historico_familiar',
    'estagio', 'tipo_tumor', 'metastase', 'tamanho_tumor_cm'
]

X = df_modelo[features]
y = df_modelo['resultado']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = RandomForestClassifier(
    n_estimators=100, max_depth=10, random_state=42
)
modelo.fit(X_train, y_train)

acuracia = accuracy_score(y_test, modelo.predict(X_test))

# -----------------------------------------------------------------------------
# DASHBOARD
# -----------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Pacientes simulados", len(df))
col2.metric("Taxa de sucesso média", f"{df['resultado'].mean()*100:.1f}%")
col3.metric("Acurácia do modelo", f"{acuracia*100:.1f}%")

st.divider()

# -----------------------------------------------------------------------------
# GRÁFICO – IMPORTÂNCIA DAS VARIÁVEIS
# -----------------------------------------------------------------------------
importancias = pd.DataFrame({
    "Variável": features,
    "Importância": modelo.feature_importances_
}).sort_values("Importância")

st.subheader("📊 Importância das Variáveis no Modelo")

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(importancias["Variável"], importancias["Importância"])
st.pyplot(fig)

# -----------------------------------------------------------------------------
# PREDIÇÃO INTERATIVA
# -----------------------------------------------------------------------------
st.divider()
st.subheader("🔮 Simular novo paciente")

c1, c2 = st.columns(2)

with c1:
    idade = st.slider("Idade", 25, 85, 55)
    sexo = st.selectbox("Sexo", ["F", "M"])
    estagio = st.selectbox("Estágio", [1, 2, 3, 4])
    tipo = st.selectbox("Tipo de Tumor", ["HR+", "HER2+", "Triplo_Negativo"])

with c2:
    historico = st.selectbox("Histórico Familiar", [0, 1])
    metastase = st.selectbox("Metástase", [0, 1])
    tamanho = st.slider("Tamanho do tumor (cm)", 0.5, 8.0, 3.0)

if st.button("Executar Predição"):
    sexo_cod = 0 if sexo == "F" else 1
    tipo_cod = {"HR+": 0, "HER2+": 1, "Triplo_Negativo": 2}[tipo]

    paciente = np.array([[idade, sexo_cod, historico, estagio, tipo_cod, metastase, tamanho]])
    prob = modelo.predict_proba(paciente)[0][1] * 100
    tratamento = atribuir_tratamento(estagio, tipo)

    st.success(f"Probabilidade de sucesso: {prob:.1f}%")
    st.write("💊 Tratamento sugerido:", tratamento)

st.caption("⚠️ Protótipo com dados simulados. Não utilizar para decisões clínicas reais.")
