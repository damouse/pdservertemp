'''
General purpose, shared routines for all projects
'''

import time


class Timer(object):

    '''
    Clocking object for benching.

    Usage:
        with Timer(key='identifyingKey'):
            #do things that need to be timed
    '''

    def __init__(self, key="", verbose=True):
        self.verbose = verbose
        self.key = key

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print self.key + ' elapsed time: %f ms' % self.msecs
