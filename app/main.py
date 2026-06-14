from fastapi import FastAPI

from app.routes.predict import router as predict_router
from app.routes.models import router as models_router

from app.database import engine
from app.models.prediction_model import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Arquitetura de Model Serving funcionando"
    }


app.include_router(predict_router)

app.include_router(models_router)