from sqlalchemy import Column, Integer, Float, String

from app.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    idade = Column(Integer)
    renda_anual = Column(Float)
    tempo_emprego = Column(Integer)

    categoria_risco = Column(String)

    valor_solicitado = Column(Float)
    taxa_juros = Column(Float)

    percentual_renda = Column(Float)

    historico_negativo = Column(Integer)

    tempo_credito = Column(Integer)

    previsao = Column(Integer)