from app import es
from flask_login import UserMixin
from elasticsearch import Elasticsearch
from peewee import Model, CharField


'''Initialise elasticsearch db if needed'''
#this needs some more work
try:
	es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
except NameError:
	es = Elasticsearch()
	'''create example user'''
	es.index(index="users", id=1, body={"id":1, "e-mail": "example@example.com"})
	'''download articles'''
	#!/usr/bin/python
	import add_new_amcatdata.py

class User(UserMixin):
	id = CharField()
	username = CharField(unique=True)
	email = CharField(unique=True)
	password_hash = CharField()
	
	def __repr__(self):
		return '<User {}>'.format(self.username)
		
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def check_password_hash(self, password):
		return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
		
