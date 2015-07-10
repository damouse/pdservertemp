'''
Builds the external API dynamically by scanning for functions that begin with 'api_' in 
pdserver.core.hub. These methods are exposed as xmlrpc methods to the internet at large. 

This is done so the hub methods can be called internally (and tested without having to boot
the server.) 

If you're poking around in here looking for something, you're in the wrong place. 
'''

from twisted.web import xmlrpc
from twisted.internet import defer
import pdserver.core.hub as hub
from pdserver.utils import *


class Base(xmlrpc.XMLRPC):

    def __init__(self, **kwargs):
        xmlrpc.XMLRPC.__init__(self, kwargs)

        # build a dict of exposed api methods
        self.apiFunctions = {k.replace('api_', ''): getattr(hub, k) for k in dir(hub) if 'api' in k}

    def lookupProcedure(self, procedurePath):
        try:
            return self.apiFunctions[procedurePath]
        except KeyError, e:
            raise xmlrpc.NoSuchFunction(self.NOT_FOUND, "procedure %s not found" % procedurePath)


def castFailure(failure):
    '''
    Converts an exception (or general failure) into an xmlrpc fault for transmission
    iff its a known issue (which is most likely a user error.) If its an unknown issue, let it
    propogate.
    '''
    # if not issubclass(exceptions.PdServerException, failure):
    #     print 'Bad exception! ' + str(failure)
    #     raise failure
    # else:
    print 'API call failure! :'
    failure.printTraceback()
    raise xmlrpc.Fault(123, failure.getErrorMessage())


def apiWrapper(target):
    '''
    Takes the target api method and adds error and success callbacks so we can intercept them as a last resort
    before they go out on the wire.
    '''
    def outside(*args):
        return target(*args).addErrback(castFailure).addCallback(castSuccess)

    return outside


def castSuccess(res):
    print "Call suceeding with result: " + str(res)
    return res
