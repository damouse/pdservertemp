'''
Command and control-- the place where all inputs, calls, methods and functionality
goes to for action.

All methods return deferreds. Calls are mixed snake and camel because the 
api module dynamically builds the calls from methods that start with 'api_'

The methods are all pure unless otherwise stated. Methods are written to be 
self-documenting unless they go nuts. 

All 'submethods,' including validation and database calls, may fail at anytime. 
They **should rely on exceptions,** since these are transparently sent back to the client.
'''

from pdserver import model
from pdserver.db import manager
from pdserver.model import names
from twisted.internet import defer

from pdtools.security import localencryption
from pdserver.utils import *


###################################################
# Authentication
###################################################

@defer.inlineCallbacks
def api_login(username, password):
    model.user.usernameValid(username)
    model.user.passwordValid(password)

    user = yield manager.getUser('username', username)

    localencryption.checkPassword(password, user['password'])

    # security considerations here

    defer.returnValue(user)


@defer.inlineCallbacks
def api_register(username, email, password):
    model.user.usernameValid(username)
    model.user.emailVaild(email)
    model.user.passwordValid(password)

    password = localencryption.hashPassword(password)
    pdid = names.idForUser(username)

    res = yield manager.createUser(username, email, password, pdid)

    # security considerations here

    defer.returnValue(res)


###################################################
# Chutes
###################################################

@defer.inlineCallbacks
def api_provisionChute(userPdid, chuteName, options):
    '''
    Register a chute as a development chute. 
    '''
    pass


@defer.inlineCallbacks
def api_publishChute(chutePdid, options):
    '''
    Publish a development chute to the store.  
    '''
    pass

@defer.inlineCallbacks
def api_installChute(userPdid, chutePdid, namespace, permissions):
    '''
    A user has requested a chute be installed. 

    Namespace defines the target routers, and is either a single router or a 
    group. This method returns valid access tokens.
    '''
    pass

###################################################
# Routers
###################################################

@defer.inlineCallbacks
def api_provisionRouter(userPdid, chuteName, routerName, options):
    '''
    Provision a router. This is a newly installed paradrop instance that needs
    to be registered, added to the namespace, etc. 
    '''
    pass


###################################################
# Misc and Utils
###################################################

@defer.inlineCallbacks
def api_echo(message):
    ''' Twisted needs at least one yield and treats it as a maybe, so there you go. '''
    yield 1
    defer.returnValue(message)
