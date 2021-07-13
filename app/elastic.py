from flask import g
from app import db
from elasticsearch import Elasticsearch
from peewee import Model, CharField, IntegerField

class User(Model):
	id = IntegerField(unique=True)
	username = CharField()
	email = CharField(unique=True)
	password = CharField()
	role = CharField()
	
	def __repr__(self):
		return '<User {}>'.format(self.id)
        

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
