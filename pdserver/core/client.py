'''
A testing file. 
'''


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
    # reactor.stop()


def printError(error):
    print 'error', error
    # reactor.stop()


def main():
    proxy = Proxy('http://localhost:7040/')

    proxy.callRemote('echo', 'hello').addCallbacks(printValue, printError)
    proxy.callRemote('tools.multiply', 6, 5).addCallbacks(printValue, printError)
    proxy.callRemote('snappy.add', 6, 5).addCallbacks(printValue, printError)

    reactor.run()

if __name__ == '__main__':
    main()
