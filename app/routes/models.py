from fastapi import APIRouter

from app.registry.model_registry import MODELS


router = APIRouter(
    tags=["Modelos"]
)


@router.get(
    "/models",
    summary="Listar modelos registrados"
)
def listar_modelos():

    modelos = []

    for nome, dados in MODELS.items():

        modelos.append({

            "name": nome,

            "algorithm": dados["algorithm"],

            "type": dados["type"],

            "version": dados["version"],

            "status": dados["status"],

            "deployment_status": dados["deployment_status"],

            "environment": dados["environment"],

            "endpoint": dados["endpoint"],

            "pipeline_status": dados["pipeline_status"],

            "rollback_available": dados["rollback_available"],

            "last_deploy": dados["last_deploy"],

            "accuracy": dados["accuracy"],

            "health": dados["health"],

            "requests_count": dados["requests_count"],

            "avg_response_ms": dados["avg_response_ms"],

            "model_size_mb": dados["model_size_mb"],

            "last_training": dados["last_training"],

            "retraining_required": dados["retraining_required"],

            "warning": dados["warning"]

        })

    return {

        "total_models": len(modelos),

        "models": modelos

    }