'''
Base and shared functionality for API methods
'''

from twisted.web import xmlrpc


class Base(xmlrpc.XMLRPC):

    def xmlrpc_echo(self, x):
        return x
