
from pdserver.db import manager
from nose.twistedtools import deferred

from twisted.internet import defer

from nose import tools


@deferred()
@defer.inlineCallbacks
def testInsert():
    user = yield manager.db.users.insert({'content': 'nothing intersting'})
    count = yield manager.db.users.count()
    assert count == 1
    yield manager.db.users.remove({"_id": user})
