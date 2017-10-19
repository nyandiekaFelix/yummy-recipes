import unittest

from yummy_recipes import APP
from yummy_recipes.models.user import User, USERS

class TestAuth(unittest.TestCase):
    ''' Helper methods '''

    def signup(self, first_name, second_name, email, password, 
                password_confirm):
        
        res = APP.test_client(self)
        return res.post('/signup', data=dict(
            first_name=first_name,
            second_name=second_name,
            email=email,
            password=password,
            password_confirm=password_confirm), 
            follow_redirects=True)

    def login(self, email, password):
        
        res = APP.test_client(self)
        return res.post('/login', data=dict(
            email=email,
            password=password), follow_redirects=True)

    ''' User Authentication Test Cases '''
    def test_user_signup(self):
        ''' Should Register New User '''

        response = self.signup("Firstish", "Secondish", "name@domain.com", 
                                "Very_1secret", "Very_1secret")
        self.assertEqual(response.status_code, 200)
 
    def test_login(self):
        ''' Should login Valid User '''

        response = self.login("name@domain.com", "Very_1secret")
        self.assertTrue(response.status_code, 200)
