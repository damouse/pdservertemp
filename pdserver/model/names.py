'''
Naming and permissions. 

All objects are identified by a human-readable UUID, which is a domain-style
identifier. 

Some of these methods are thin simply to wrap the underlying logic. 
'''


class Name(object):

    """ Light wrapper around UUID names"""

    def __init__(self, uuid):
        self.uuid = uuid
        self.type = None

    def __repr__(self):
        return formatHuman(self.uuid)


def formatHuman(uuid):
    ''' Return a nicely formatted version of this uuid '''
    return uuid


def formatMachine(uuid):
    ''' Return the absolute machine version of this name'''
    return uuid


def idForUser(username):
    return 'pd.' + username


def idForChute(username, chuteName, buildNumber):
    return idForUser(username) + '.chutes.' + chuteName + '-' + str(buildNumber)


def idForRouter(username, routerName):
    return idForUser(username) + '.routers.' + routerName


def idForInstance(username, routerName, chuteName, buildNumber):
    return idForRouter(username) + '.instances.' + chuteName + '-' + str(buildNumber)
