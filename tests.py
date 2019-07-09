import unittest

from app import app


class TestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
    
    def tearDown(self):
        pass

    def test_hello_world(self):
        expected_response = b'Hello, World!'
        response = self.app.get('/hello/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), expected_response)

if __name__ == '__main__':
    unittest.main()
