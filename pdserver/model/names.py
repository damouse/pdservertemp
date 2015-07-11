'''
Naming and permissions. 

All objects are identified by a human-readable UUID, which is a domain-style
identifier. There are two versions of the identifier: a concise human-readable version 
and a fully-qualified name. 

All PDID's are prefaced with a top-level name. This currently serves no purpose 
other than to make it obvious when a PDID appears, but could be used later
for alternative namespacing (development mode, 3rd party servers, etc). 

Each subdomain has a declarative portion in the machine version to clear up 
ambiguity. This is removed in the human version except where there are collisions. 
Additionally, chutes get their version appended-- this is automagically added
unless specified. 

Examples:
    User 'damouse':
        Machine: pd.damouse
        Human: pd.damouse

    Chute 'netflix' on build 12:
        Machine: pd.damouse.chutes.netflix.12
        Human: pd.damouse.netflix

    Router 'aardvark':
        Machine: pd.damouse.routers.aardvark
        Human: pd.damouse.aardvark

    Chute instance 'netflix':
        Machine: pd.damouse.routers.aardvark.instances.netflix.12
        Human: pd.damouse.aardvark.netflix

    Router group 'daisy':
        Machine: pd.damouse.groups.daisy.routers.aardvark.instances.netflix.12
        Human: pd.damouse.daisy.aardvark.netflix

Note the additional 'router' namespace in the fully-qualified name in grouped
instances. This is added for consistency, not namespacing

Human versions can have namespace collisions that have to be detected. 
Full ids cannot have namespace collisions by definition. This has a few consequences:
    Chute names must be unique
    Owned router names must be unique
        pd.damouse.aardvark and pd.mikedabike.aardvark is fine-- different owners
    Owned group names must be unique
        Same as above
'''

###################################################
# Formatting
###################################################


def formatHuman(uuid):
    '''
    Return a nicely formatted version of this uuid

    TODO: deal with namespace collisions.
    '''
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


def idForGroup(username, groupName):
    return idForUser(username) + '.groups.' + groupName


def idForInstance(username, routerName, chuteName, buildNumber):
    return idForRouter(username, routerName) + '.instances.' + chuteName + '-' + str(buildNumber)
