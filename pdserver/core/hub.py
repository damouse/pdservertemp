'''
Command and control-- the place where all inputs, calls, methods and functionality
goes to for action.

All methods here return deferreds.
'''

import pdserver.model as model
import pdserver.db.manager as manager
from twisted.internet import defer

from pdtools.security import localencryption
from pdserver.utils import exceptions


###################################################
# API Core Functions
###################################################


@defer.inlineCallbacks
def login(email, password):
    '''
    Validate user credentials. Validation methods raise errors 
    that propogate back up deferred chain, no need to check them.
    '''

    print 'Loading User'

    model.user.emailVaild(email)
    model.user.passwordValid(password)

    # check db for user object
    user = yield manager.getUserByEmail(email)

    # check password
    if not localencryption.checkPassword(password, user['password']):
        raise exceptions.InvalidPassword("Passwords do not match")

    # create or retrieve access token and return it

    # temp just for testing
    user.pop('_id', None)
    print user

    print 'Returning user'
    defer.returnValue(user)


@defer.inlineCallbacks
def register(email, password):
    model.user.emailVaild(email)
    model.user.passwordValid(password)

    password = localencryption.hashPassword(password)

    res = yield manager.createUser(email, password)

    # login authentication things here
    defer.returnValue(res)


def checkinInstance():
    '''
    Registers a live chute instance, indicating its alive and has a connection with the 
    backend. 
    '''
    pass


def checkinChuteInstance():
    pass
