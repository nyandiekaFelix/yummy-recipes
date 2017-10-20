import random

USERS = {}
    
class User(object):
    ''' User model '''
    def __init__(self, email, first_name, second_name, password):
        ''' Initialize user '''
        self.user_id = random.randint(1, 1000)
        self.email = email
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        