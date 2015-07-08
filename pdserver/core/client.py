'''
A testing file. 
'''

import time


from twisted.web.xmlrpc import Proxy
from twisted.internet import reactor
from twisted.internet import defer

startTime = None


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


def clock(stuff):
    print 'Bench: ' + str((time.time() - startTime) * 1000) + 'ms'


def kill(stuff):
    from twisted.internet import reactor
    reactor.stop()


def main():
    proxy = Proxy('http://localhost:7040/', allowNone=True)

    # Benching txmongo
    n = 1
    global startTime
    startTime = time.time()

    defs = []
    print 'Synchronous--'

    # base tests
    # for i in range(n):
    #     defs.append(proxy.callRemote('instantiate', 1000).addCallbacks(printValue, printError))

    # defer.DeferredList(defs).addCallback(clock).addCallback(kill)

    print 'Asynchronous--'
    startTime = time.time()
    defs = []

    # base tests
    for i in range(n):
        defs.append(proxy.callRemote('instantiateTx', 1000).addCallbacks(printValue, printError))

    defer.DeferredList(defs).addCallback(clock).addCallback(kill)

    # raw testing
    # defs.append(proxy.callRemote('instantiateTx', 1000).addCallbacks(printValue, printError))

    # Testing the proxy calls
    # proxy.callRemote('echo', 'hello').addCallbacks(printValue, printError)
    # proxy.callRemote('tools.multiply', 6, 5).addCallbacks(printValue, printError)
    # proxy.callRemote('snappy.add', 6, 5).addCallbacks(printValue, printError)

    # drop the test db
    # proxy.callRemote('dropTest').addCallbacks(printValue, printError)

    reactor.run()

if __name__ == '__main__':
    main()
