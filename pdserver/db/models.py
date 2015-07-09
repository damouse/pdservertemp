'''
Model objects. These are thin, homebaked ORM objects. 
'''

import pdserver.utils.logger.out as out


class Base(object):

    '''
    Base object for all model classes

    self.contents is the mongo (and json) representation of the object. The fields are not unpacked 
    for the sake of performance-- this is a very light ORM wrapping.
    '''

    def __init__(self, contents={}):
        super(Base, self).__init__()

        self.contents = contents

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, contents):
        self._contents = contents
