'''
Model operations for users.
'''

from validate_email import validate_email
from pdserver.utils import exceptions


def passwordValid(password):
    """
    Validate a password. 

    :param password: Password to check
    :raises: InvalidPassword 
    """
    if len(password) < 8:
        raise exceptions.InvalidPassword("Password too short")


def emailVaild(email):
    """
    Validate an email. Does not check if the email is taken in the database. 

    :param password: Password to check
    :type str:
    :raises: InvalidEmail 
    """
    if not validate_email(email):
        raise exceptions.InvalidEmail("Email is invalid")
