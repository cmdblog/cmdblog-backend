"""docstring
API test
"""

import json
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


class VersionTests(TestCase):
    """
    /version のテスト
    """

    def test_version_returns_version(self):
        """
        /version が 200で、versionを返す
        """

        response = self.client.get('/version')
        self.assertEqual(response.status_code, 200)

        returned_json = json.loads(response.content)
        self.assertEqual(returned_json['version'], "DUMMY_VERSION")
