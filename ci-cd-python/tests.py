import unittest 
import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data) 

if __name__ == '__main__':
    unittest.main()
