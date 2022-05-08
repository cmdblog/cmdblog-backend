"""docstring
API test
"""
from django.test import TestCase


class RootTests(TestCase):
    """docstring
    全般的なテストについておこなう。
    """

    def test_root_returns_200(self):
        """docstring
        'URL/' は200レスポンスを返す。
        """

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
