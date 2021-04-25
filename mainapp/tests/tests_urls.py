from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainapp.views import index


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('mainapp:index')
        self.assertEquals(resolve(url).func, index)