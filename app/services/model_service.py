import joblib
import pandas as pd

from app.logger import logger

from app.models.prediction_model import Prediction
from app.database import SessionLocal

dados_modelo = joblib.load("app/model/modelo_inadimplencia.pkl")

modelo = dados_modelo["modelo"]


def realizar_previsao(dados_entrada):

    categoria_transformada = dados_modelo["ordinal_encoder"].transform(
        [[dados_entrada.categoria_risco]]
    )[0][0]

    dados = pd.DataFrame([{
        "idade": dados_entrada.idade,
        "renda_anual": dados_entrada.renda_anual,
        "tempo_emprego": dados_entrada.tempo_emprego,
        "categoria_risco": categoria_transformada,
        "valor_solicitado": dados_entrada.valor_solicitado,
        "taxa_juros": dados_entrada.taxa_juros,
        "percentual_renda": dados_entrada.percentual_renda,
        "historico_negativo": dados_entrada.historico_negativo,
        "tempo_credito": dados_entrada.tempo_credito,
        "tempo_emprego_missing": 0,
        "taxa_juros_missing": 0,
        "tipo_moradia_OTHER": 0,
        "tipo_moradia_OWN": 1,
        "tipo_moradia_RENT": 0,
        "objetivo_emprestimo_EDUCATION": 0,
        "objetivo_emprestimo_HOMEIMPROVEMENT": 0,
        "objetivo_emprestimo_MEDICAL": 0,
        "objetivo_emprestimo_PERSONAL": 1,
        "objetivo_emprestimo_VENTURE": 0
    }])

    previsao = int(modelo.predict(dados)[0])
    logger.info(f"Previsão realizada com sucesso: {previsao}")

    db = SessionLocal()

    nova_previsao = Prediction(
        idade=dados_entrada.idade,
        renda_anual=dados_entrada.renda_anual,
        tempo_emprego=dados_entrada.tempo_emprego,
        categoria_risco=dados_entrada.categoria_risco,
        valor_solicitado=dados_entrada.valor_solicitado,
        taxa_juros=dados_entrada.taxa_juros,
        percentual_renda=dados_entrada.percentual_renda,
        historico_negativo=dados_entrada.historico_negativo,
        tempo_credito=dados_entrada.tempo_credito,
        previsao=previsao
    )

    db.add(nova_previsao)
    db.commit()
    db.close()

    return previsao