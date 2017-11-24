''' This file contains utility functions '''

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
