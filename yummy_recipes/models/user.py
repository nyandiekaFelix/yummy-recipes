''' User model '''

class User(object):
    
    def __init__(self, email, first_name, second_name, password):
        ''' Initialize user '''
        self.email = email
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
        
    

    