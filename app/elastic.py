from app import es
from elasticsearch import Elasticsearch

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

	
	
