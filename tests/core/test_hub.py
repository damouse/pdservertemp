from pdserver.core import hub
from pdserver.db import manager
from pdserver.utils import *

from nose.twistedtools import deferred
from pdserver.core import hub
from pdserver.db import manager
from nose import tools

from twisted.internet import defer


manager.db = manager.Manager(mode='test')

# Refactor these tests!


@deferred()
@defer.inlineCallbacks
def testRegisterSuceeds():
    yield hub.api_register('damouse', 'damouse123@gmail.com', '12344567')
    count = yield manager.db.users.find({'username': 'damouse'})
    assert len(count) == 1
    manager.db.drop()


@deferred()
@defer.inlineCallbacks
def testRegisterBadEmail():
    ex = None
    try:
        yield hub.api_register('damouse', 'damouse123gmail.com', '12344567')
    except InvalidCredentials, e:
        ex = e

    assert ex != None
    manager.db.drop()


@deferred()
@defer.inlineCallbacks
def testRegisterBadUsername():
    ex = None
    try:
        yield hub.api_register('1', 'damouse123@gmail.com', '12344567')
    except InvalidCredentials, e:
        ex = e

    assert ex != None
    manager.db.drop()
