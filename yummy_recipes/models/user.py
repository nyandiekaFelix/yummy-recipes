''' User Model '''

USERS = {}


class User(object):
    ''' User model '''
    def __init__(self, email, password):
        ''' Initialize user '''
        self.email = email
        self.password = password
        self.categories = {}

    def __repr__(self):
        return 'User: {}'.format(self.email)
