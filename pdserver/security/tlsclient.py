'''
See here: http://stackoverflow.com/questions/28677455/use-tls-and-python-for-authentication
'''

# tlsclient.py
from twisted.python.filepath import FilePath
from twisted.internet.endpoints import SSL4ClientEndpoint
from twisted.internet.ssl import PrivateCertificate, Certificate, optionsForClientTLS
from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet.task import react
from twisted.internet.protocol import Protocol, Factory

import sys


class SendAnyData(Protocol):

    def connectionMade(self):
        self.deferred = Deferred()
        self.transport.write(b"HELLO\r\n")

    def connectionLost(self, reason):
        self.deferred.callback(None)


@inlineCallbacks
def main(reactor, name):
    pem = FilePath(name.encode("utf-8") + b".client.private.pem").getContent()
    caPem = FilePath(b"ca-private-cert.pem").getContent()
    clientEndpoint = SSL4ClientEndpoint(
        reactor, u"localhost", 4321,
        optionsForClientTLS(u"the-authority", Certificate.loadPEM(caPem), PrivateCertificate.loadPEM(pem)),
    )
    proto = yield clientEndpoint.connect(Factory.forProtocol(SendAnyData))
    yield proto.deferred


if __name__ == '__main__':
    react(main, sys.argv[1:])
