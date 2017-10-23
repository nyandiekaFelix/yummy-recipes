import unittest

from yummy_recipes import APP
from yummy_recipes.models.user import User, USERS

class TestAuth(unittest.TestCase):
    ''' Helper methods '''

    def login(self, email, password):
        
        res = APP.test_client(self)
        return res.post('/login', data=dict(
            email=email,
            password=password), follow_redirects=True)

    def test_login(self):
        ''' Should login Valid User '''

        response = self.login("name@domain.com", "Very_1secret")
        self.assertTrue(response.status_code, 200)
