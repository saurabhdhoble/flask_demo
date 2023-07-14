from tests.base_case import BaseTestCase
import json


class TestQuotes(BaseTestCase):
    def test_get_quote(self):
        response = self.client.get(f"/v1/quotes/gandalf/quote", headers=self.headers)
        self.assertEqual(response.status_code, 200, response.data)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['success'], "Success")

