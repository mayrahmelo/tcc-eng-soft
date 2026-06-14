from pydantic import BaseModel
from typing import List


class DadosEntrada(BaseModel):
    features: List[float]