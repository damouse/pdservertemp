'''
User Model Objects.
'''

def userValid(contents):
	'''
	Return true if this is a valid user document

	:param contents: JSON representation of the user model
	:type contents: str.
	:returns: True if the user is valid, False if not 
	'''
	return True

def userRegister(email, password):
	''' 
	Create an account.

	:param email: user's email
	:type email: str.
	:param password: user's password
	:type password: str.
	:returns: tuple -- (True, UserDocument) if successful, else (False, Error) otherwise
	'''
	return False, None