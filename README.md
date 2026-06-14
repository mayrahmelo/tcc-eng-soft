# Arquitetura Operacional para Deploy e Gerenciamento de Modelos Preditivos via API

Projeto desenvolvido como Trabalho de Conclusão de Curso (TCC) do MBA em Engenharia de Software.

A solução propõe uma arquitetura operacional voltada ao deploy, monitoramento e gerenciamento de múltiplos modelos preditivos através de APIs REST desacopladas, utilizando práticas modernas de Engenharia de Software, observabilidade e integração contínua.

---

# Objetivo do Projeto

O objetivo deste projeto é demonstrar a construção de uma arquitetura operacional capaz de disponibilizar modelos preditivos em ambiente desacoplado, permitindo:

* gerenciamento centralizado de modelos
* execução de inferências via API
* monitoramento operacional
* observabilidade arquitetural
* deploy cloud
* integração contínua (CI/CD)
* suporte a múltiplos modelos preditivos

A arquitetura foi desenvolvida utilizando princípios de modularidade, separação de responsabilidades e desacoplamento entre serviços.

---

# Arquitetura da Solução

A solução foi estruturada em múltiplas camadas operacionais:

* FastAPI para construção da API REST
* Streamlit para dashboard operacional
* SQLite para persistência de inferências
* GitHub Actions para integração contínua
* Render para deploy cloud
* Docker para containerização da aplicação

A arquitetura permite gerenciamento centralizado de múltiplos modelos preditivos registrados dinamicamente via registry.

---

# Funcionalidades Implementadas

* API REST para execução de inferências
* Arquitetura multi-modelo desacoplada
* Registry centralizado de modelos
* Dashboard operacional com Streamlit
* Monitoramento e observabilidade
* Persistência de histórico de inferências
* Logging operacional
* Integração contínua com GitHub Actions
* Deploy cloud automatizado
* Documentação Swagger/OpenAPI
* Gerenciamento operacional de modelos

---

# Modelos Implementados

A arquitetura foi validada utilizando múltiplos modelos preditivos:

| Modelo                   | Tipo          | Algoritmo           |
| ------------------------ | ------------- | ------------------- |
| Risco de Crédito         | Classificação | Random Forest       |
| Cancelamento de Conta    | Classificação | Random Forest       |
| Detecção de Fraude       | Classificação | XGBoost             |
| Aprovação de Empréstimos | Classificação | Logistic Regression |
| Avaliação Imobiliária    | Regressão     | Linear Regression   |

---

# Estrutura do Projeto

```bash
/app
    /models
    /registry
    /routes
    /schemas
    /services

/tests

.github/workflows

dashboard.py
requirements.txt
README.md
```

---

# Execução Local

## Backend FastAPI

```bash
uvicorn app.main:app --reload
```

API disponível em:

```bash
http://127.0.0.1:8000/docs
```

---

## Dashboard Operacional

```bash
streamlit run dashboard.py
```

Dashboard disponível em:

```bash
http://localhost:8501
```

---

# Deploy Cloud

## Swagger / API Online

https://tcc-eng-soft.onrender.com/docs

---

## Dashboard Operacional Online

https://tcc-dashboard-sknj.onrender.com

---

# CI/CD

O projeto utiliza GitHub Actions para execução automatizada de:

* instalação de dependências
* validação do ambiente
* execução de testes automatizados
* verificação de estabilidade da aplicação

A integração contínua permite validação automática da arquitetura a cada novo commit realizado no repositório.

---

# Observabilidade Operacional

O dashboard operacional foi desenvolvido para centralizar informações relacionadas à arquitetura, incluindo:

* métricas operacionais
* latência média
* volume de requisições
* status dos modelos
* gerenciamento de deploy
* monitoramento operacional
* indicadores de CI/CD

As métricas operacionais foram simuladas arquiteturalmente com o objetivo de demonstrar a capacidade da plataforma de centralizar informações de monitoramento e governança dos modelos.

---

# Tecnologias Utilizadas

* Python
* FastAPI
* Streamlit
* SQLite
* SQLAlchemy
* Scikit-learn
* XGBoost
* Docker
* GitHub Actions
* Render
* Pandas
* Pytest

---

# Resultados Obtidos

A solução desenvolvida permitiu validar:

* desacoplamento entre modelos e aplicações clientes
* gerenciamento centralizado de múltiplos modelos
* deploy operacional em ambiente cloud
* observabilidade arquitetural
* integração entre API e dashboard operacional
* integração contínua automatizada
* organização modular da arquitetura backend

---

# Autora

Mayra Melo Silva

MBA em Engenharia de Software

---

# Orientação

Vinicius Santos Andrade
