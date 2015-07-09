"""Paradrop server.

Usage:
    pdserver start <host> <port> <github-url> 
    paradrop snap-install <host> <port>
    paradrop (-h | --help)
    paradrop --version
Options:
    -h --help     Show this screen.
    --version     Show version.
"""

'''
This is the entry point and the hub for main functionality. All methods called by the api
are exposed here. The other modules implement their functionality in a thin way and do not
crosstalk. 
'''

from docopt import docopt
import twisted
from twisted.web import xmlrpc, server

from pdserver.api import base, pdsnappy, pdtools
import pdserver.model as model

PORT = 7040


###################################################
# API Core Functions
###################################################

def loginUser(email, password):
    '''
    Validate user credentials. Validation methods raise errors 
    that propogate back up deferred chain, no need to check them.
    '''
    model.user.emailVaild(email)
    model.user.passwordValid(password)

    #check db for user object

    #create or retrieve access token and return it 

    return 'asdf'


def registerUser(email, password):
    model.user.emailVaild(email)
    model.user.passwordValid(password)


def checkinInstance():
    '''
    Registers a live chute instance, indicating its alive and has a connection with the 
    backend. 
    '''
    pass


def checkinChuteInstance():
    pass

###################################################
# Booting and Initialization
###################################################


def main():
    # Skipping args for now
    # args = docopt(__doc__, version='Paradrop build tools v0.1')
    # print(args)

    # if args['install']:
    #     installChute(args['<host>'], args['<port>'], args['<github-url>'])

    # if args['snap-install']:
    #     print 'Not implemented. Sorry, love.'

    print 'Starting Server'
    from twisted.internet import reactor

    # Get the heirarchical servers and assign them under the base object
    r = base.Base(allowNone=True)
    r.putSubHandler('snappy', pdsnappy.Snappy())
    r.putSubHandler('tools', pdtools.Tools())

    reactor.listenTCP(PORT, server.Site(r))
    reactor.run()


###################################################
# Random testing code
###################################################

def TEST():
    # pipe()
    pass


def pipe():
    '''
    This may be the easiest way to get the main pd instance to end gracefully 
    Now we have to make it Twisted, non-blocking, and non-polling
    '''
    import os
    import time

    pipe_path = "/tmp/mypipe"
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
    # Open the fifo. We need to open in non-blocking mode or it will stalls until
    # someone opens it for writting
    pipe_fd = os.open(pipe_path, os.O_RDONLY | os.O_NONBLOCK)

    with os.fdopen(pipe_fd) as pipe:
        while True:
            message = pipe.read()
            if message:
                print("Received: '%s'" % message)
            # print("Doing other stuff")
            time.sleep(0.5)

if __name__ == '__main__':
    TEST()
    # main()
