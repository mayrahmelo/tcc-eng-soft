from fastapi import APIRouter, HTTPException

from app.schemas.predict_schema import DadosEntrada
from app.services.model_service import realizar_previsao
from app.registry.model_registry import MODELS


router = APIRouter()


@router.post("/predict/{model_name}")
def predict(model_name: str, dados: DadosEntrada):

    if model_name not in MODELS:
        raise HTTPException(
            status_code=404,
            detail="Modelo não encontrado"
        )

    resultado = realizar_previsao(model_name, dados)

    return {
        "modelo": model_name,
        "previsao": resultado
    }