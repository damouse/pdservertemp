'''
Base and shared functionality for API methods
'''

from twisted.web import xmlrpc
import pdserver.db
import txmongo

from twisted.internet import defer


class Base(xmlrpc.XMLRPC):

    def xmlrpc_echo(self, x):
        return x

    def xmlrpc_instantiate(self, n):
        ''' A new router instance just came up. Save it.  '''
        man = pdserver.db.Manager(mode='test')

        for i in range(0, n):
            man.db.instances.insert_one({
                'name': 'John',
                'age': '23',
                'password': '12345678',
            })

        # This isn't needed most likely, but the proxy doesn't like dealing with None
        return True

    def xmlrpc_instantiateTx(self, n):
        ''' A new router instance just came up. Save it.  '''

        print 'Starting Async DB'

        def dummy(res):
            print 'Finished insert'
            return True

        def insert(conn):
            print "inserting data..."
            collection = conn.test.instances

            for x in range(n):
                d = collection.insert({
                    'name': 'John',
                    'age': '23',
                    'password': '12345678',
                }, safe=True)

            return d.addCallback(dummy)

        d = txmongo.MongoConnectionPool()
        return d.addCallback(insert)
        return d

        man = pdserver.db.Manager(mode='test')

        for i in range(0, n):
            man.db.instances.insert_one({
                'name': 'John',
                'age': '23',
                'password': '12345678',
            })

        # This isn't needed most likely, but the proxy doesn't like dealing with None
        return True

    def xmlrpc_dropTest(self):
        ''' Drop the test db '''
        man = pdserver.db.Manager(mode='test')
        man.client.drop_database('test')

        return True

    def xmlrpc_test(self):
        def hi(res):
            return 'Hi!'

        d = defer.Deferred()
        d.addCallback(hi)
        return d.callback(True)
