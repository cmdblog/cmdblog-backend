
from django.test import TestCase
from django.utils import timezone


class RootTests(TestCase):
    def test_root_returns_200(self):
        """
        'URL/' は200レスポンスを返す。
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
