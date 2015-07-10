
import pdserver.model.user as user
from pdserver.utils import *
from nose.tools import assert_raises


def testBadPassword():
    assert_raises(InvalidCredentials, user.passwordValid, 'asd')


def testGoodPassword():
    user.passwordValid("verynicelongpassword")


def testGoodEmail():
    user.emailVaild('damousea@gmail.com')


def testBadEmail():
    assert_raises(InvalidCredentials, user.emailVaild, 'asd')
    assert_raises(InvalidCredentials, user.emailVaild, 'asd@')
    assert_raises(InvalidCredentials, user.emailVaild, '@gmail.com')
