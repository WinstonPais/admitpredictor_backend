import unittest
from mainapp.helperFunctions import getModel

class TestGetModelFunction(unittest.TestCase):

    def test_getsModel(self):

        from pathlib import Path
        import joblib

        ML_MODELS_FOLDER = Path(__file__).resolve().parent.parent.parent.joinpath('Ml_models')
        model = joblib.load(ML_MODELS_FOLDER.joinpath('sklearn_LinearRegression').joinpath('sklearn_LinearRegression.pkl'))
        self.assertEqual(type(getModel('sklearn_LinearRegression')), type(model))
        self.assertEqual(getModel('rubbish'), None)