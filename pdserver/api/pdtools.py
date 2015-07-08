'''
Paradrop build tools api methods.

Authentication badly needed.
'''

from twisted.web import xmlrpc


class Tools(xmlrpc.XMLRPC):

    def xmlrpc_multiply(self, a, b):
        return a * b
