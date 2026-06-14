from pydantic import BaseModel

class DadosEntrada(BaseModel):
    idade: int
    renda_anual: float
    tempo_emprego: int
    categoria_risco: str
    valor_solicitado: float
    taxa_juros: float
    percentual_renda: float
    historico_negativo: int
    tempo_credito: int
