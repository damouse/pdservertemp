
import pdserver.db


class TestModels:

    def setup(self):
        self.db = pdserver.db.Manager(mode='test')

    def teardown(self):
        self.db.client.drop_database('test')

    def testCreate(self):
        self.db.users.insert_one({
            'name': 'John',
            'age': '23',
            'password': '12345678',
        })

        assert self.db.users.count() == 1
        user = self.db.users.find_one()
        assert user['name'] == 'John'


class TestUsers:

    def setup(self):
        self.db = pdserver.db.Manager(mode='test')

    def teardown(self):
        self.db.client.drop_database('test')

    def testCreate(self):
        self.db.users.insert_one({
            'name': 'John',
            'age': '23',
            'password': '12345678',
        })

        assert self.db.users.count() == 1
        user = self.db.users.find_one()
        assert user['name'] == 'John'
