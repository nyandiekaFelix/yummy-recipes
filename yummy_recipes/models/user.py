''' User model '''

class User(object):
    EMAIL = ''
    FIRST_NAME = ''
    SECOND_NAME = ''
    USERNAME = ''
    PASSWORD = ''

    def __init__(self):
        ''' Initialize user '''
        self.email = None
        self.first_name = None
        self.second_name = None
        self.password = None
        self.model = None

    def create_user(self, username, first_name, second_name, email, password):
        
        username = first_name + '_' + second_name
        email = email
        password = password

        self.model.__setattr__(self.model.FIRST_NAME, first_name)
        self.model.__setattr__(self.model.SECOND_NAME, second_name)
        self.model.__setattr__(self.model.USERNAME, username)
        self.model.__setattr__(self.model.EMAIL, email)
        self.model.__setattr__(self.model.PASSWORD, password)

        return self.model

    @property
    def get_email(self):
        ''' email getter '''
        return getattr(self, User.EMAIL)

    @property
    def get_first_name(self):
        ''' first name getter '''
        return getattr(self, User.FIRST_NAME)

    @property
    def get_second_name(self):
        ''' second name getter '''
        return getattr(self, User.SECOND_NAME)

    @property
    def get_username(self):
        ''' username getter '''
        return getattr(self, User.USERNAME)

    def __repr__(self):
        return '<%(username)s obj>' % dict(username=self.get_username)
