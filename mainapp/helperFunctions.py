from pathlib import Path
import joblib

ML_MODELS_FOLDER = Path(__file__).resolve().parent.parent.joinpath('Ml_models')

def getModel(algorithm):
    try:
        model = joblib.load(ML_MODELS_FOLDER.joinpath(f'{algorithm}').joinpath(f'{algorithm}.pkl'))
    except:
        return None

    return model

def getParametersFromQueryString(request, parameters):
    inputParameters = { parameter : None for parameter in parameters} 
    validQueryString = True

    for parameter in parameters:
        try:
            inputParameters[parameter] = request.GET.get(f'{parameter}')
        except:
            inputParameters[parameter] = None
            validQueryString = False

    return inputParameters, validQueryString