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


class Base(xmlrpc.XMLRPC):

    def xmlrpc_authentication(self, email, password):
        return hub.login(email, password).addErrback(castFailure)

    def xmlrpc_echo(self, x):
        return x

    # def xmlrpc_instantiate(self, n):
    #     ''' A new router instance just came up. Save it.  '''
    #     print 'vanilla'

    #     man = pdserver.db.Manager(mode='test')

    #     for i in range(n):
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
    ''' Converts an exception (or general failure) into an xmlrpc fault for transmission '''
    raise xmlrpc.Fault(123, failure.getErrorMessage())


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


# def done(res):
#     reactor.stop()

# if __name__ == '__main__':
#     log.startLogging(sys.stdout)

#     global mongo
#     mongo = txmongo.MongoConnection().callback(None)

#     example(100).addCallback(done)

#     from twisted.internet import reactor
#     reactor.run()
