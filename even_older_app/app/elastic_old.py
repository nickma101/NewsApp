from flask import g
from app import db
from elasticsearch import Elasticsearch
from peewee import Model, CharField, IntegerField

SECRET_KEY = 123

class User(Model):
	#id = IntegerField(unique=True)
	username = CharField()
	email = CharField(unique=True)
	password = CharField()
	#role = CharField()
	
	class Meta:
		database = db
		
	def create_token(self, expiration: int = None):
		"""
		Create a new token for this user
		"""
		s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=expiration)
		return s.dumps({'id': self.id})        

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def create_user(username: str, email: str, password: str) -> User:
    """
    Create and return a new User with the given information
    """
    return User.create(id = id, username = username, email=email, password=hash_password(password), role= role)


def verify_user(email: str, password: str):
    """
    Check that this user exists and can be authenticated with the given password, returning a User object
    :param email: Email address identifying the user
    :param password: Password to check
    :return: A User object if user could be authenticated, None otherwise
    """
    logging.info("Attempted login: {email}".format(**locals()))
    try:
        user = User.get(User.email == email)
    except User.DoesNotExist:
        logging.warning("User {email} not found!".format(**locals()))
        return None
    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode("utf-8")):
        return user
    else:
        logging.warning("Incorrect password for user {email}".format(**locals()))


def verify_token(token: str):
    """
    Check the token and return the authenticated user email
    :param token: The token to verify
    :return: a User object if user could be authenticated, None otherwise
    """
    s = TimedJSONWebSignatureSerializer(SECRET_KEY)
    try:
        result = s.loads(token)
    except (SignatureExpired, BadSignature):
        logging.exception("Token verification failed")
        return None
    logging.warning("TOKEN RESULT: {}" .format(result))
    return User.get(User.id == result['id'])

#def get_db():
#    if 'db' not in g:
#        g.db = es
#    return g.db

#def close_db(e=None):
#    db = g.pop('db', None)

#    if db is not None:
#        db.close()

#def init_db():
#    db = get_db()
    
        
'''Initialise elasticsearch db if needed'''
#this needs some more work
try:
	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
except NameError:
	es = Elasticsearch()
	'''create example user'''
	es.index(index="users", id=1, body={"id":1, "e-mail": "example@example.com"})
