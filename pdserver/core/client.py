import xmlrpclib

# def main():
#     s = xmlrpclib.Server('http://localhost:7090/')
#     print 'echo: ' + s.echo("lala")
#     print 'add: ' + str(s.add(1, 2))
#     print 'time: ' + str(s.date.time())


from twisted.web.xmlrpc import Proxy
from twisted.internet import reactor


class Thing:

    def __init__(self):
        self.name = "Hello!"
        self.age = 12

    def __repr__(self):
        return 'Im a thing! Name: ' + self.name + ' age: ' + str(self.age)


def printValue(value):
    print repr(value)
    reactor.stop()


def printError(error):
    print 'error', error
    reactor.stop()


def main():
    proxy = Proxy('http://localhost:7060/')
    proxy.callRemote('object').addCallbacks(printValue, printError)
    reactor.run()

if __name__ == '__main__':
    main()
