import unittest
from web import app

class CheckResponse(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def test_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()