from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainapp.views import index, tensorflowNeuralNetworks


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('mainapp:index')
        self.assertEquals(resolve(url).func, index)

    # def test_sklearnLinearRegression_url_is_resolved(self):
    #     url = reverse('mainapp:sklearnLinearRegression')
    #     self.assertEquals(resolve(url).func, sklearnLinearRegression)

    def test_tensorflowNeuralNetworks_url_is_resolved(self):
        url = reverse('mainapp:tensorflowNeuralNetworks')
        self.assertEquals(resolve(url).func, tensorflowNeuralNetworks)