'''
Exceptions and their subclasses

TODO: Distill these down and make a heirarchy.
'''


class PdServerException(Exception): pass


class InteralException(Exception): pass


class InvalidPassword(PdServerException): pass


class UserExists(PdServerException): pass


class UserDoesntExists(PdServerException): pass


class InvalidPassword(PdServerException): pass


class InvalidEmail(PdServerException): pass
