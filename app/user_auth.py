import logging
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature
from peewee import Model, CharField
from app import es

class User():
    id = CharField()
    email = CharField(unique=True)
    password = CharField()
    
    class Meta:
        database = es
		
    def create_token(self, expiration: int = None) -> str:
        """
        Create a new token for this user
        """
        s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

def verify_token(token: str):
    """
    Check the token and return the authenticated user id
    :param token: The token to verify
    :return: a User object if user could be authenticated, None otherwise
    """
    s = TimedJSONWebSignatureSerializer(SECRET_KEY)
    try:
        result =s.loads(token)
    except (SignatureExpired, BadSignature):
        logging.exception("Token verification failed")
        return None
    logging.warning("TOKEN RESULT: {}" .format(result))
    return User.get(User.id == result['id'])
