'''
Base and shared functionality for API methods.

If this file is still noisy, its because it contains a whole bit of testing code.
'''

from twisted.web import xmlrpc
import txmongo

from twisted.internet import defer

# temp
from twisted.python import log
import sys

import pdserver.core.hub as hub
from pdserver.utils import exceptions


class Base(xmlrpc.XMLRPC):

    def xmlrpc_login(self, email, password):
        return hub.login(email, password).addErrback(castFailure).addCallback(castSuccess)

    def xmlrpc_register(self, email, password):
        return hub.register(email, password).addErrback(castFailure)

    def xmlrpc_echo(self, x):
        return x

    # def xmlrpc_instantiate(self, n):
    #     ''' A new router instance just came up. Save it.  '''
    #     print 'vanilla'

    #     man = pdserver.db.Manager(mode='test')

    #     for i in range(`n):
    #         man.db.instances.insert_one({
    #             'name': 'John',
    #             'age': '23',
    #             'password': '12345678',
    #         })

    # def xmlrpc_instantiateTx(self, n):
    #     ''' A new router instance just came up. Save it.  '''
    #     print 'txMongo'
    #     return example(n)

    # def xmlrpc_dropTest(self):
    #     ''' Drop the test db '''
    #     print 'Dropping Test'
    #     man = pdserver.db.Manager(mode='test')
    #     man.client.drop_database('test')

    #     return True


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


def castSuccess(res):
    ''' likely not needed '''
    print "Call suceeding with result: " + str(res)
    return res

# mongo = None


# @defer.inlineCallbacks
# def example(n):
# insert some data
#     for x in range(n):
#         result = yield mongo.test.instances.insert({'name': 'John', 'age': '23', 'password': '12345678', }, safe=True)

#         print result

#     count = yield mongo.test.instances.count()

#     print count
#     yield True


# def addToQueue(res):
#     print 'Result found.'


# @defer.inlineCallbacks
# def sync():
# import Queue
# q = Queue.Queue()

# mongo.test.instances.insert({'name': 'John', 'age': '23', 'password': '12345678', }, safe=True).addCallback(addToQueue)
# print 'done'
# d.addBoth(q.put)
# return q.get()


# def done(res):
#     reactor.stop()

# if __name__ == '__main__':
# log.startLogging(sys.stdout)

#     global mongo
#     mongo = txmongo.MongoConnection().callback(None)

# print sync()

# example(100).addCallback(done)

#     from twisted.internet import reactor
#     reactor.run()
