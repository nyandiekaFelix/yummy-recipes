import random

USERS = {}
    
class User(object):
    ''' User model '''
    def __init__(self, email, password):
        ''' Initialize user '''
        self.email = email
        self.password = password
        self.categories = {}
        self.recipes = {}
    
    def __repr__(self):
        return '<%(email)s obj>' % dict(email=self.email)