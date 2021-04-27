# from django.test import TestCase, Client
# from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestView(APITestCase):

    def test_index_view_status_code(self):

        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_index_view_json_data(self):

        response = self.client.get('')
        expectedResponse = {
            'message' : 'Hello AWS Lambda From GitHub Actions!!!'
        }
        self.assertEqual(response.json(), expectedResponse)
