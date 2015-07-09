'''
A testing file.
'''

import time


from twisted.web.xmlrpc import Proxy
from twisted.internet import reactor
from twisted.internet import defer

startTime = None


class RpcClient:

    '''
    Remote client RPC wrapper. Translates seemingly local calls
    into remote RPC calls.

    Will aleays return deferreds
    '''

    def __init__(self, url):
        self.proxy = Proxy(url, allowNone=True)

    def __getattr__(self, item):
        def wrap(args):
            return self.proxy.callRemote(item, args)

        return wrap


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


def sync(isSynchronous, proxy, n):
    global startTime
    startTime = time.time()

    defs = []
    print 'Synchronous--'

    command = 'instantiate' if isSynchronous else 'instantiateTx'

    # base tests
    for i in range(n):
        defs.append(proxy.callRemote(command, 100).addCallbacks(printValue, printError))

    defer.DeferredList(defs).addCallback(clock).addCallback(kill)


def main():
    rpcClient = RpcClient('http://localhost:7020/')
    # proxy = Proxy('http://localhost:7020/', allowNone=True)

    rpcClient.echo('hey').addCallbacks(printValue, printError).addCallback(lambda ign: reactor.stop())

    # Benching txmongo
    # sync(False, proxy, 1000)

    # Testing the proxy calls
    # proxy.callRemote('echo', 'hello').addCallbacks(printValue, printError)
    # proxy.callRemote('tools.multiply', 6, 5).addCallbacks(printValue, printError)
    # proxy.callRemote('snappy.add', 6, 5).addCallbacks(printValue, printError)

    # drop the test db
    # proxy.callRemote('dropTest').addCallbacks(printValue, printError).addCallback(lambda ign: reactor.stop())

    reactor.run()

if __name__ == '__main__':
    main()
