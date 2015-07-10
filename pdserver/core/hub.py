'''
Command and control-- the place where all inputs, calls, methods and functionality
goes to for action.

All methods here return deferreds.
'''

import pdserver.model as model
from twisted.internet import defer

db = None


###################################################
# API Core Functions
###################################################

@defer.deferredGenerator
def login(email, password):
    '''
    Validate user credentials. Validation methods raise errors 
    that propogate back up deferred chain, no need to check them.
    '''
    model.user.emailVaild(email)
    model.user.passwordValid(password)

    # check db for user object

    # create or retrieve access token and return it

    yield 'asdf'


def registerUser(email, password):
    model.user.emailVaild(email)
    model.user.passwordValid(password)


def checkinInstance():
    '''
    Registers a live chute instance, indicating its alive and has a connection with the 
    backend. 
    '''
    pass


def checkinChuteInstance():
    pass
