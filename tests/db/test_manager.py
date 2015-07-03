
import pdserver.db


def testManagerValid():
    ''' Manager object can be created '''
    dbMan = pdserver.db.Manager(mode='development')
    assert(dbMan is not None)


def testInsert():
    dbMan = pdserver.db.Manager(mode='test')

    entry = {'content': 'nothing intersting'}
    entries = dbMan.db.entries

    entries.insert_one(entry)

    assert entries.count() == 1

    # not a great idea to put this here, eh
    dbMan.client.drop_database('test')


def testDropCollection():
    dbMan = pdserver.db.Manager(mode='test')

    entry = {'content': 'nothing intersting'}
    entries = dbMan.db.entries

    entries.insert_one(entry)

    assert entries.count() == 1

    # not a great idea to put this here, eh
    dbMan.client.test.entries.drop()

    assert entries.count() == 0


#####
# Stubs
#####

stubDb = None


def createStubDatabase():
    stubDb = pdserver.db.Manager(mode='test')
    return stubDb


def removeStubDatabase():
    stubDb.client.drop_database('test')
    stubDb = None
