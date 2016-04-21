

from Basic_endPoints import app

import unittest
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test2(self):
        response = self.get_Response('/')
        assert 'Hello' == response

    def get_Response(self,symbol):
        return self.app.get(symbol).data

    def get_my_name_test(self):
        response = self.get_Response('/test2')
        assert response == 'Lev2'



