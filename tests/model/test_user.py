
import pdserver.model.user as user
from nose.tools import assert_raises


def testBadPassword():
    assert_raises(user.InvalidPassword, user.passwordValid, 'asd')


def testGoodPassword():
    user.passwordValid("verynicelongpassword")


def testGoodEmail():
    user.emailVaild('damousea@gmail.com')


def testBadEmail():
    assert_raises(user.InvalidEmail, user.emailVaild, 'asd')
    assert_raises(user.InvalidEmail, user.emailVaild, 'asd@')
    assert_raises(user.InvalidEmail, user.emailVaild, '@gmail.com')
