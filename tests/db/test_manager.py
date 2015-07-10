
from pdserver.db import manager
from twisted.internet import defer

# NOTE: none of the deferreds work! Have to make them sync in order to test it


def testManagerValid():
    ''' Manager object can be created '''
    dbMan = manager.Manager(mode='development')
    assert(dbMan is not None)


@defer.inlineCallbacks
def testInsert():
    dbMan = manager.Manager(mode='test')

    entry = {'content': 'nothing intersting'}
    entries = dbMan.db.entries

    yield entries.insert(entry)
    count = yield entries.count()
    assert count == 1

    # not a great idea to put this here, eh
    dbMan.client.drop_database('test')


# def testDropCollection():
#     dbMan = manager.Manager(mode='test')

#     entry = {'content': 'nothing intersting'}
#     entries = dbMan.db.entries

#     entries.insert_one(entry).addCallback(success).addErrback(fail)

#     # not a great idea to put this here, eh
#     block_on(dbMan.client.test.entries.drop())

#     count = block_on(entries.count())
#     assert count == 0


# class TestModels:

#     def setup(self):
#         self.db = manager.Manager(mode='test')

#     def teardown(self):
#         self.db.client.drop_database('test')

#     def testCreate(self):
#         self.create()

#     @defer.inlineCallbacks
#     def create(self):
#         yield self.db.users.insert_one({
#             'name': 'John',
#             'age': '23',
#             'password': '12345678',
#         })

#         assert False

#         count = yield self.db.users.count()
#         assert count == 1

#         user = yield self.db.users.find_one()
#         assert user['name'] == 'John'


# #####
# Stubs
# #####

stubDb = None


def createStubDatabase():
    stubDb = manager.Manager(mode='test')
    return stubDb


def removeStubDatabase():
    stubDb.client.drop_database('test')
    stubDb = None


# #####
# Testing
# #####
# import Queue


# def success(res):
#     print 'Succes! ' + str(res)
#     return 2


# def fail(res):
#     print 'Fail!' + str(res)
#     return True


# def block_on(d, timeout=None):
#     q = Queue.Queue()
#     d2 = defer.Deferred().addBoth(q.put)

#     d.addCallback(success).addErrback(fail)
#     d.chainDeferred(d2)

#     return q.get(timeout=1)
