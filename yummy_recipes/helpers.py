''' This file contains utility functions used to carry out operations on data '''

def lower_email(email):
    ''' This method converts an email into lowercase before storage so 
        as to avoid duplicates based on the string's case.
    '''

    email_name, domain_part = email.strip().rsplit('@', 1)
    email = '@'.join([email_name.lower(), domain_part.lower()])
    
    return email

def lower_name(name):
    ''' This method converts a category or recipe name into lowercase before 
        storage so as to avoid duplicates based on the string's case
    '''
    return name.lower()

def check_for_duplicate(obj, value_string):
    ''' This method checks if a value exists in an object '''
    exists = False

    for key, key_id in obj.items():
        if value_string in key_id.__dict__.values():
            exists = True
            break
        else:
            exists = False

    return exists
