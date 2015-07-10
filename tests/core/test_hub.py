from pdserver.core import hub
from pdserver.db import manager

from nose.twistedtools import deferred
from pdserver.core import hub
from pdserver.db import manager
from nose import tools

from twisted.internet import defer


manager.db = manager.Manager(mode='test')


def end(res):
    manager.db.drop()
    return res


def call(res):
    return manager.db.users.find({'username': 'damouse'})


@deferred()
def testRegisterSuceeds():
    return registerSuceeds().addBoth(end)


@defer.inlineCallbacks
def registerSuceeds():
    yield hub.api_register('damouse', 'damouse123@gmail.com', '12344567')
    count = yield manager.db.users.find({'username': 'damouse'})
    assert len(count) == 1


# @deferred()
# def testRegisterSuceeds():
#     d = hub.api_register('damouse', 'damouse123@gmail.com', '12344567')

#     d.addCallback(call)
#     d.addCallback(lambda x: tools.eq_(len(x), 1))
#     d.addBoth(end)

#     return d


# @deferred()
# def testRegisterFails():
#     d = hub.api_register('damouse', 'damouse123@gmail.com', '12344567')
#     d.addCallback(manager.db.users.find, {'username': 'damouse'})
#     d.addCallback(lambda x: tools.eq_(len(x), 10))
#     d.addCallback(lambda x: manager.db.drop())

#     return d
