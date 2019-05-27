import unittest
from web import app

class TestAskMe(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def tearDown(self):
        pass
    def test_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    def test_num_docs(self):
        pass