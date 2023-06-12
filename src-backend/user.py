
'''
This Class is to hold the info of a User when the user has been pulled from the database
'''

class User:
    def __init__(self, is_debug):
        if is_debug:
            print( " User Class ")