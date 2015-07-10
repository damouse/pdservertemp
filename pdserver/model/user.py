'''
Model operations for users. They all raise exceptions instead of returning 
errors, mostly because it makes the deferred code very pretty. 
'''

from validate_email import validate_email
from pdserver.utils import *


def passwordValid(password):
    if len(password) < 8:
        raise InvalidCredentials("Password too short")


def emailVaild(email):
    if not validate_email(email):
        raise InvalidCredentials("Email is invalid")


def usernameValid(name):
    if len(name) < 6:
        raise InvalidCredentials("Password too short")
