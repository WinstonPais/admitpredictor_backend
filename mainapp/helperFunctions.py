from pathlib import Path
import joblib
from tensorflow.keras.models import load_model

ML_MODELS_FOLDER = Path(__file__).resolve().parent.parent.joinpath('Ml_models')

def getModel(algorithm):
    model = None
    try:
        # if algorithm == "sklearn_LinearRegression":
        #     model = joblib.load(ML_MODELS_FOLDER.joinpath(f'{algorithm}').joinpath(f'{algorithm}.pkl'))
        # elif algorithm == "tensorflow_neuralNetworks":
            model = load_model(ML_MODELS_FOLDER.joinpath(f'{algorithm}').joinpath(f'{algorithm}.h5'))
    except:
        return None

    return model
