# from django.test import TestCase, Client
# from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestIndexView(APITestCase):

    def test_index_view_status_code(self):

        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_index_view_json_data(self):

        response = self.client.get('')
        expectedResponse = {
            'message' : 'Hello AWS Lambda From GitHub Actions!!!'
        }
        self.assertEqual(response.json(), expectedResponse)

class TestSklearnLinearRegressionView(APITestCase):

    def test_SklearnLinearRegression_view_status_code(self):

        response = self.client.get('/sklearn_LinearRegression/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/sklearn_LinearRegression/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_SklearnLinearRegression_view_json_data_success(self):

        response = self.client.get('/sklearn_LinearRegression/?GREScore=337&TOEFLScore=118&UniversityRating=4&SOP=4.5&LOR=4.5&CGPA=9.65&Research=1')
        
        self.assertEqual(response.json()['success'], True)

    def test_SklearnLinearRegression_view_json_data_Invalid(self):

        response = self.client.get('/sklearn_LinearRegression/?blablabla=ggff')
        
        self.assertEqual(response.json()['success'], False)