import unittest
from mainapp.helperFunctions import getModel
from tensorflow.keras.models import load_model

class TestGetModelFunction(unittest.TestCase):

    def test_getsModel(self):

        from pathlib import Path
        import joblib

        ML_MODELS_FOLDER = Path(__file__).resolve().parent.parent.parent.joinpath('Ml_models')
        model = load_model(ML_MODELS_FOLDER.joinpath('tensorflow_neuralNetworks').joinpath('tensorflow_neuralNetworks.h5'))
        self.assertEqual(type(getModel('tensorflow_neuralNetworks')), type(model))
        self.assertEqual(getModel('rubbish'), None)