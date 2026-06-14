import joblib
import numpy as np

from app.registry.model_registry import MODELS
from app.logger import logger


def realizar_previsao(model_name, dados_entrada):

    model_info = MODELS[model_name]

    modelo_path = model_info["path"]

    modelo = joblib.load(modelo_path)

    features = np.array(dados_entrada.features).reshape(1, -1)

    # Verifica se o modelo possui scaler
    if "scaler" in model_info:

        scaler = joblib.load(model_info["scaler"])

        features = scaler.transform(features)

    previsao = modelo.predict(features)[0]

    # Conversão para tipos compatíveis com JSON
    if isinstance(previsao, np.integer):
        previsao = int(previsao)

    elif isinstance(previsao, np.floating):
        previsao = float(previsao)

    logger.info(
        f"Previsão realizada com sucesso | Modelo: {model_name} | Resultado: {previsao}"
    )

    return previsao