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
This is the entry point to the server and handles all initialization. 
pdserver.core.hub is where all functionality is implemented. 
'''

from docopt import docopt
import twisted
from twisted.web import xmlrpc, server

from . import api
import pdserver.db.manager
import pdserver.core.hub

PORT = 7020


###################################################
# Booting and Initialization
###################################################


def main(port=PORT):
    # Skipping args for now
    # args = docopt(__doc__, version='Paradrop build tools v0.1')
    # print(args)

    # if args['install']:
    #     installChute(args['<host>'], args['<port>'], args['<github-url>'])

    # if args['snap-install']:
    #     print 'Not implemented. Sorry, love.'


    # boot the database
    pdserver.db.manager.db = pdserver.db.manager.Manager(mode='development')

    # Get the heirarchical servers and assign them under the base object
    r = api.Base(allowNone=True)

    from twisted.internet import reactor
    reactor.listenTCP(PORT, server.Site(r))
    reactor.run()


###################################################
# Random testing code
###################################################


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
    main()
