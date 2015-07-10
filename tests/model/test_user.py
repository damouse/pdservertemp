
import pdserver.model.user as user
from pdserver.utils import exceptions
from nose.tools import assert_raises


def testBadPassword():
    assert_raises(exceptions.InvalidCredentials, user.passwordValid, 'asd')


def testGoodPassword():
    user.passwordValid("verynicelongpassword")


def testGoodEmail():
    user.emailVaild('damousea@gmail.com')


def testBadEmail():
    assert_raises(exceptions.InvalidCredentials, user.emailVaild, 'asd')
    assert_raises(exceptions.InvalidCredentials, user.emailVaild, 'asd@')
    assert_raises(exceptions.InvalidCredentials, user.emailVaild, '@gmail.com')
