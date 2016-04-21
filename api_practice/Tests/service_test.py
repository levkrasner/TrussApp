import unittest

from service import  app

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test2(self):
        response = self.get_Response('/')
        assert 'Hello' == response

    def test_something(self):
        assert 1==1

if __name__ == '__main__':
    unittest.main()
