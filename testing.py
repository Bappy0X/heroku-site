import unittest
from web import create_app

app = create_app()

class CheckResponse(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_index(self):
        response = self.client.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()