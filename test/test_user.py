import unittest
from yummy_recipes.models.user import UserController, User

class TestUserCtrl(unittest.TestCase):
    ''' Test User Controller class '''
    
    def __init__(self):
        ''' create instance of controller '''
        self.user_instance = User()
        self.user = {
            'email': 'some_email@domain.com',
            'first_name': 'Firstish',
            'second_name': 'Secondish',
            'password': 'shh_its_a_secret'
        }
    # def initialize(self):
       
    
    def test_user_is_valid(self):
        ''' check if user has all required details '''
        self.assertTrue(isinstance(self.user_instance, self.user))

    def test_missing_email(self):
        ''' raise error when email is missing '''
        self.assertRaises(ValueError,
                          self.user_instance.create_user,
                          first_name='firstish',
                          second_name='secondish',
                          password='very_secret')

    def test_missing_first_name(self):
        ''' raise error when first name is missing '''
        self.assertRaises(ValueError,
                          self.user_instance.create_user,
                          email='emailish@domain.com',
                          second_name='secondish',
                          password='very_secret')

    def test_missing_second_name(self):
        ''' raise error when second name is missing '''
        self.assertRaises(ValueError,
                          self.user_instance.create_user,
                          email='emailish@domain.com',
                          first_name='firstish',
                          password='very_secret')

    def test_missing_password(self):
        ''' raise error when password not given '''
        self.assertRaises(ValueError,
                          self.user_instance.create_user,
                          email='emailish@domain.com',
                          first_name='firstish',
                          second_name='secondish')