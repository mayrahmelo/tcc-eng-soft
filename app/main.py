from fastapi import FastAPI

from app.routes.predict import router as predict_router
from app.routes.models import router as models_router

from app.database import engine
from app.models.prediction_model import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Arquitetura Operacional para Modelos Preditivos",
    description="""
    API responsável pelo deploy, monitoramento e gerenciamento
    de múltiplos modelos preditivos em arquitetura desacoplada.
    """,
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Arquitetura operacional para deploy e gerenciamento de modelos preditivos funcionando"
    }


app.include_router(predict_router)

app.include_router(models_router)