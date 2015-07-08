'''
Base and shared functionality for API methods.

If this file is still noisy, its because it contains a whole bit of testing code.
'''

from twisted.web import xmlrpc
import pdserver.db
import txmongo

from twisted.internet import defer

# temp
import time
from twisted.python import log
import sys


class Base(xmlrpc.XMLRPC):

    def xmlrpc_authentication(self, email, password):
        '''
        Authenticate the user and return some method of identifying him or herself
        '''

        pass

    def xmlrpc_echo(self, x):
        return x

    def xmlrpc_instantiate(self, n):
        ''' A new router instance just came up. Save it.  '''
        print 'vanilla'

        man = pdserver.db.Manager(mode='test')

        for i in range(n):
            man.db.instances.insert_one({
                'name': 'John',
                'age': '23',
                'password': '12345678',
            })

    def xmlrpc_instantiateTx(self, n):
        ''' A new router instance just came up. Save it.  '''
        print 'txMongo'
        return example(n)

    def xmlrpc_dropTest(self):
        ''' Drop the test db '''
        print 'Dropping Test'
        man = pdserver.db.Manager(mode='test')
        man.client.drop_database('test')

        return True

    def xmlrpc_test(self):
        def hi(res):
            return 'Hi!'

        d = defer.Deferred()
        d.addCallback(hi)
        return d.callback(True)

@defer.inlineCallbacks
def example(n):
    mongo = yield txmongo.MongoConnection()

    foo = mongo.test  # `foo` database
    test = foo.instances  # `test` collection

    # insert some data
    for x in range(n):
        result = yield test.insert({'name': 'John', 'age': '23', 'password': '12345678',
            }, safe=True)

        print result

    yield True

if __name__ == '__main__':
    log.startLogging(sys.stdout)
    example().addCallback(lambda ign: reactor.stop())

    from twisted.internet import reactor
    reactor.run()
