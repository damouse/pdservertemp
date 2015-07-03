'''
Database connection manager. Need one of these to do anything relating to the underlaying database.

Does it make sense to make multiple connection objects to the database? Does that impact performance?
'''

from pymongo import MongoClient


class Manager(object):

    def __init__(self, mode='dev'):
        '''
        Mode is one of ['test', 'development', 'production']
        '''

        # create a connection to the mongodb
        self.client = MongoClient()
        self.mode = mode

        # Pick the right database
        if mode == 'development':
            self.db = self.client.development
        elif mode == 'production':
            self.db = self.client.production
        elif mode == 'test':
            self.db = self.client.test
        else:
            raise SyntaxError("Mode must be one of ['development', 'production', 'test']. the input " + mode + " is invalid.")

        # Pull refs for easier access later (and to declare them for anyone reading this)
        # Is this necesary?
        self.users = self.db.users

    def drop():
        ''' Drops the active database. Be careful '''
        self.client.drop_database(self.mode)
