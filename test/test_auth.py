import unittest

from yummy_recipes import APP
from yummy_recipes.models.user import User, USERS

class TestAuth(unittest.TestCase):

    def setUp(self):
        APP.config['WTF_CSRF_ENABLED'] = False
   
    def test_login(self):
        ''' Should login Valid User '''
        res = APP.test_client(self)
        response = res.post('/login', data=dict(
            email="name@domain.com",
            password="Very_1secret"), follow_redirects=True) 

        self.assertTrue(response.status_code, 200) 

    def test_signup(self):
        ''' Should register User '''
        res = APP.test_client(self)
        response = res.post('/signup', data=dict(
            email="email@domain.com",
            password="Very_1secret"), follow_redirects=True)

        self.assertTrue(response.status_code, 200)

    def test_invalid_password(self):
        ''' Should return error due to invalid password '''
        res = APP.test_client(self)
        response = res.post('/login', data=dict(
            email="name@domain.com",
            password=None), follow_redirects=True)

        self.assertTrue(response.status_code, 401)
    
    def test_invalid_email(self):
        ''' Should return error due to invalid email '''
        res = APP.test_client(self)
        response = res.post('/login', data=dict(
            email=None,
            password="Very_1secret"), follow_redirects=True)

        self.assertTrue(response.status_code, 401)

