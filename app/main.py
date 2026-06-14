from fastapi import FastAPI

from app.routes.predict import router

from app.database import engine
from app.models.prediction_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API do TCC funcionando"}


app.include_router(router)