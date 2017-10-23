import unittest
from yummy_recipes.models.user import User, USERS

class TestUser(unittest.TestCase):
    ''' Test User Controller class '''
    
    def test_user_creation(self):
        ''' create instance of controller '''
        sample_user = User('some_email@domain.com', 'shh_its_a_secret')
        USERS[sample_user] = sample_user
        self.assertEqual(1, len(USERS))
    