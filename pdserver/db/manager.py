'''
Database connection manager. Need one of these to do anything relating to the underlaying database.

Does it make sense to make multiple connection objects to the database? Does that impact performance?
'''

from pymongo import MongoClient
from twisted.internet import defer
import txmongo

from pdserver.utils import *


# Module access to the database object. Initialzied in core.main.main. References to this
# object should never leave the module
db = None


class Manager(object):

    def __init__(self, mode='test'):
        '''
        Mode is one of ['test', 'development', 'production']
        '''

        # create a connection to the mongodb. None passed to trigger right away
        self.client = txmongo.MongoConnection(pool_size=100)
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
        self.users = self.db.users
        self.routers = self.db.routers
        self.chutes = self.db.chutes

        self.routerInstances = self.db.routerInstances
        self.chuteInstances = self.db.chuteInstances

    def drop(self):
        ''' Drops the active database syncrhonously. Be careful out there. '''
        MongoClient().drop_database(self.mode)


# I think these should go in their own files, but while there are only a few of them I'm leaving them here
@defer.inlineCallbacks
def createUser(email, password):
    '''
    Creates a user given their email and password.

    :raises: AuthenticationError
    '''
    yield db.users.find({'email': email})
    count = yield db.users.count()

    if count != 0:
        raise AuthenticationError("A user with that email already exists")

    res = yield db.users.insert({'email': email, 'password': password})
    defer.returnValue(res)


@defer.inlineCallbacks
def getUser(key, value):
    '''
    Searches user database using passed key and value. Expects the key to be unique (like email or username)
    or will raise a ValueError

    :param query: the dictionary to query the database with
    :type query: dict.
    :raises: AuthenticationError, ValueError
    '''
    user = yield db.users.find({key: value})

    if not user:
        raise AuthenticationError("User with key " + key + " not found")

    if len(user) != 1:
        raise ValueError('Key ' + key + ' is not useful for uniquely identifying a user.')

    defer.returnValue(user[0])
