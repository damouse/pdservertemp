from pdserver.core import hub
from pdserver.db import manager

from nose.twistedtools import deferred

from nose import tools


# @deferred()
# def testInsert():
#     man = manager.Manager(mode='test')

#     d = man.users.insert({'content': 'nothing intersting'})
#     d.addCallback(man.users.count)
#     d.addCallback(lambda x: tools.eq_(x, 1))
#     d.addCallback(lambda x: man.drop())

#     return d
