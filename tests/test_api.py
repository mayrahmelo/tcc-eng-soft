from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "API do TCC funcionando"
    }


def test_predict():

    dados = {
        "idade": 30,
        "renda_anual": 50000,
        "tempo_emprego": 5,
        "categoria_risco": "B",
        "valor_solicitado": 10000,
        "taxa_juros": 12.5,
        "percentual_renda": 0.2,
        "historico_negativo": 0,
        "tempo_credito": 3
    }

    response = client.post("/predict", json=dados)

    assert response.status_code == 200

    resultado = response.json()

    assert "previsao" in resultado