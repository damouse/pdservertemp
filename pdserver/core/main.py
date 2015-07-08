'''
Paradrop server v2.

Entry point into the server. Imports protocols/resources from toolsapi and pdapi
and starts the server here. All database interaction is handled in the db package
'''

import twisted
import time
from twisted.web import xmlrpc, server
import client


class Example(xmlrpc.XMLRPC):

    """
    An example object to be published.
    """

    def xmlrpc_echo(self, x):
        """
        Return all passed args.
        """
        return x

    def xmlrpc_add(self, a, b):
        """
        Return sum of arguments.
        """
        return a + b

    def xmlrpc_object(self):
        stuff = client.Thing()
        return stuff


class Date(xmlrpc.XMLRPC):

    """
    Serve the XML-RPC 'time' method.
    """

    def xmlrpc_time(self):
        """
        Return UNIX time.
        """
        return time.time()

if __name__ == '__main__':
    print 'Starting Server'
    from twisted.internet import reactor
    r = Example()
    date = Date()
    r.putSubHandler('date', date)
    reactor.listenTCP(7060, server.Site(r))
    reactor.run()
