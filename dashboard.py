import streamlit as st
import requests
import pandas as pd

API_URL = "https://tcc-eng-soft.onrender.com/models"

st.set_page_config(
    page_title="Dashboard de Gerenciamento de Modelos Preditivos",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("🚀 Dashboard de Gerenciamento de Modelos Preditivos")

st.markdown(
    """
    Arquitetura operacional para deploy, monitoramento
    e gerenciamento de modelos preditivos via API.
    """
)

st.caption(
    "Arquitetura operacional desacoplada com gerenciamento centralizado de modelos preditivos."
)

# ==========================================
# CONSUMO API
# ==========================================

response = requests.get(API_URL)

dados = response.json()

modelos = dados["models"]

df = pd.DataFrame(modelos)

# ==========================================
# NOMES VISUAIS
# ==========================================

nomes_visuais = {

    "credito": "Risco de Crédito",

    "churn": "Cancelamento de Conta",

    "fraude": "Detecção de Fraude",

    "loan_approval": "Aprovação de Empréstimos",

    "house_price": "Avaliação Imobiliária"

}

df["display_name"] = df["name"].map(
    nomes_visuais
)

# ==========================================
# KPIs
# ==========================================

total_modelos = len(df)

modelos_ativos = len(
    df[df["deployment_status"] == "deployed"]
)

media_latencia = round(
    df["avg_response_ms"].mean(),
    1
)

total_requests = int(
    df["requests_count"].sum()
)

healthy_models = len(
    df[df["health"] == "Healthy"]
)

warning_models = len(
    df[df["health"] != "Healthy"]
)

classification_models = len(
    df[df["type"] == "classification"]
)

regression_models = len(
    df[df["type"] == "regression"]
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(
    "📦 Modelos",
    total_modelos
)

col2.metric(
    "✅ Deployados",
    modelos_ativos
)

col3.metric(
    "⚡ Latência Média",
    f"{media_latencia} ms"
)

col4.metric(
    "📈 Requisições",
    total_requests
)

col5.metric(
    "🟢 Operacionais",
    healthy_models
)

col6.metric(
    "🟡 Alertas",
    warning_models
)

# ==========================================
# TIPOS MODELOS
# ==========================================

tipo_col1, tipo_col2 = st.columns(2)

tipo_col1.info(
    f"📊 Modelos de Classificação: {classification_models}"
)

tipo_col2.info(
    f"📈 Modelos de Regressão: {regression_models}"
)

st.divider()

# ==========================================
# ARQUITETURA APIs
# ==========================================

st.subheader("🔌 Arquitetura de APIs")

api_df = pd.DataFrame({

    "Modelo": df["display_name"],

    "Endpoint": df["endpoint"],

    "Ambiente": df["environment"],

    "Status Deploy": df["deployment_status"]

})

st.dataframe(
    api_df,
    use_container_width=True
)

st.divider()

# ==========================================
# CI/CD
# ==========================================

st.subheader(
    "⚙️ Gerenciamento de Deploy e CI/CD"
)

cicd_df = pd.DataFrame({

    "Modelo": df["display_name"],

    "Pipeline CI/CD": [
        "Estável" for _ in range(len(df))
    ],

    "Rollback": [
        "Habilitado" for _ in range(len(df))
    ],

    "Último Deploy": df["last_deploy"]

})

st.dataframe(
    cicd_df,
    use_container_width=True
)

st.divider()

# ==========================================
# OBSERVABILIDADE
# ==========================================

st.subheader(
    "📈 Observabilidade Operacional"
)

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        "#### Latência Média por Modelo"
    )

    latency_df = pd.DataFrame({

        "Modelo": df["display_name"],

        "Latência": df["avg_response_ms"]

    })

    st.bar_chart(
        latency_df.set_index("Modelo")
    )

with col2:

    st.markdown(
        "#### Requisições por Modelo"
    )

    requests_df = pd.DataFrame({

        "Modelo": df["display_name"],

        "Requisições": df["requests_count"]

    })

    st.bar_chart(
        requests_df.set_index("Modelo")
    )

st.divider()

# ==========================================
# MONITORAMENTO MODELOS
# ==========================================

st.subheader(
    "📊 Monitoramento Operacional dos Modelos"
)

for modelo in modelos:

    display_name = nomes_visuais.get(
        modelo["name"],
        modelo["name"]
    )

    with st.container(border=True):

        col1, col2 = st.columns([3, 1])

        # ==========================================
        # INFORMAÇÕES
        # ==========================================

        with col1:

            st.markdown(
                f"## {display_name}"
            )

            st.write(
                f"**Algoritmo:** {modelo['algorithm']}"
            )

            st.write(
                f"**Tipo:** {modelo['type']}"
            )

            st.write(
                f"**Versão:** {modelo['version']}"
            )

            st.write(
                f"**Endpoint:** {modelo['endpoint']}"
            )

            st.write(
                f"**Último treinamento:** {modelo['last_training']}"
            )

            st.write(
                f"**Último deploy:** {modelo['last_deploy']}"
            )

            st.write(
                f"**Tamanho do modelo:** {modelo['model_size_mb']} MB"
            )

        # ==========================================
        # MÉTRICAS
        # ==========================================

        with col2:

            st.metric(
                "Métrica do Modelo",
                modelo["accuracy"]
            )

            st.metric(
                "Latência",
                f"{modelo['avg_response_ms']} ms"
            )

            st.metric(
                "Requisições",
                modelo["requests_count"]
            )

        # ==========================================
        # STATUS
        # ==========================================

        st.markdown(
            "### Status Operacional"
        )

        status_col1, status_col2, status_col3 = st.columns(3)

        with status_col1:

            st.success(
                "✅ Deploy Ativo"
            )

        with status_col2:

            if modelo["health"] == "Healthy":

                st.success(
                    "🟢 Status Operacional"
                )

            elif modelo["health"] == "Monitoring":

                st.warning(
                    "🟡 Atenção Operacional"
                )

            else:

                st.error(
                    "🔴 Ambiente Instável"
                )

        with status_col3:

            if modelo["retraining_required"]:

                st.error(
                    "🔄 Retreinamento Necessário"
                )

            else:

                st.success(
                    "✅ Modelo Estável"
                )

        # ==========================================
        # PIPELINE
        # ==========================================

        st.markdown(
            "### Pipeline de Deploy"
        )

        cicd_col1, cicd_col2 = st.columns(2)

        with cicd_col1:

            st.info(
                "🚀 Pipeline CI/CD: Estável"
            )

        with cicd_col2:

            st.success(
                "↩️ Rollback Habilitado"
            )

        # ==========================================
        # ALERTAS
        # ==========================================

        st.markdown(
            "### Observações Operacionais"
        )

        if modelo["health"] == "Monitoring":

            st.error(
                modelo["warning"]
            )

        else:

            st.info(
                modelo["warning"]
            )

        st.divider()

# ==========================================
# FOOTER
# ==========================================

st.caption(
    "Projeto acadêmico desenvolvido para demonstração de arquitetura operacional para gerenciamento de modelos preditivos."
)