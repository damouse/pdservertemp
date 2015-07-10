
# spin up a server on a different thread

import pdserver.core.main as main
from pdtools.coms.client import RpcClient
import multiprocessing
from twisted.internet import defer

import Queue

PORT = 12345

# Need to wait for the deferred and have a live server. Not sure about this one. 
# class TestBaseApi:

#     def setup(self):
#         self.server = multiprocessing.Process(target=main.main, kwargs={'port': PORT})
#         self.client = RpcClient('http://localhost:' + str(PORT) + '/')

#     def teardown(self):
#         # self.server.terminate()
#         self.client = None

#     def testBadParams(self):
#         # assert_raises(user.InvalidEmail, user.emailVaild, 'asd')
#         q = Queue.Queue()
#         self.client.authentication('damouse@gmail.com', '12345678').addBoth(q.put)

#         res = q.get()
#         print res
#         assert False


# def success(res):
#     print 'Succes!'
#     return res


# def block_on(d, timeout=None):
#     q = Queue()
#     d.addBoth(q.put)
#     ret = q.get()
#     # except Empty:
#     #     raise Timeout
#     # if isinstance(ret, Failure):
#     #     ret.raiseException()
#     # else:
#     return ret
