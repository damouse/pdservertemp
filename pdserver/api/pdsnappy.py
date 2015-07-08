'''
Paradrop instance API methods. 

Authentication needed.
'''

from twisted.web import xmlrpc


class Snappy(xmlrpc.XMLRPC):

    def xmlrpc_add(self, a, b):
        return a + b
