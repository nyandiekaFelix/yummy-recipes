import unittest
from yummy_recipes.models.user import User, USERS

class TestUser(unittest.TestCase):
    ''' Test User Controller class '''
    
    def test_user_creation(self):
        ''' create instance of controller '''
        sample_user = User('some_email@domain.com', 'Firstish', 
                           'Secondish', 'shh_its_a_secret')
        USERS.append(sample_user)
        self.assertEqual(1, len(USERS))
    