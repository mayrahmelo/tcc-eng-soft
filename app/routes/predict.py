from fastapi import APIRouter
from app.schemas.predict_schema import DadosEntrada
from app.services.model_service import realizar_previsao

router = APIRouter()

@router.post("/predict")
def predict(dados: DadosEntrada):

    resultado = realizar_previsao(dados)

    return {
        "previsao": resultado
    }
