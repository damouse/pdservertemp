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


from docopt import docopt
import twisted
from twisted.web import xmlrpc, server

from pdserver.api import base, pdsnappy, pdtools

PORT = 7020


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


def TEST():
    '''
    This is a sandbox.
    '''

    from pdserver.utils.general import Timer

    with Timer(key='Unsync'):
        print 'hi'

if __name__ == '__main__':
    # TEST()
    main()
