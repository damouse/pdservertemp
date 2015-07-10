
import pdserver.db
from twisted.internet import defer


def testManagerValid():
    ''' Manager object can be created '''
    dbMan = pdserver.db.Manager(mode='development')
    assert(dbMan is not None)


@defer.inlineCallbacks
def testInsert():
    dbMan = pdserver.db.Manager(mode='test')

    entry = {'content': 'nothing intersting'}
    entries = dbMan.db.entries

    yield entries.insert(entry)
    count = yield entries.count()
    assert count == 1

    # not a great idea to put this here, eh
    dbMan.client.drop_database('test')


@defer.inlineCallbacks
def testDropCollection():
    dbMan = pdserver.db.Manager(mode='test')

    entry = {'content': 'nothing intersting'}
    entries = dbMan.db.entries

    yield entries.insert_one(entry)

    # not a great idea to put this here, eh
    yield dbMan.client.test.entries.drop()

    count = yield entries.count()
    assert count == 0


class TestModels:

    def setup(self):
        self.db = pdserver.db.Manager(mode='test')

    def teardown(self):
        self.db.client.drop_database('test')

    @defer.inlineCallbacks
    def testCreate(self):
        yield self.db.users.insert_one({
            'name': 'John',
            'age': '23',
            'password': '12345678',
        })

        count = yield self.db.users.count()
        assert count == 1

        user = yield self.db.users.find_one()
        assert user['name'] == 'John'


# #####
# Stubs
# #####

stubDb = None


def createStubDatabase():
    stubDb = pdserver.db.Manager(mode='test')
    return stubDb


def removeStubDatabase():
    stubDb.client.drop_database('test')
    stubDb = None
