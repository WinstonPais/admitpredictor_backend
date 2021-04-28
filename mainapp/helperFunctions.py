from pathlib import Path
import joblib

ML_MODELS_FOLDER = Path(__file__).resolve().parent.parent.joinpath('Ml_models')

def getModel(algorithm):
    try:
        model = joblib.load(ML_MODELS_FOLDER.joinpath(f'{algorithm}').joinpath(f'{algorithm}.pkl'))
    except:
        return None

    return model