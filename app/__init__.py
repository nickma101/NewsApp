from flask import Flask
from elasticsearch import Elasticsearch

app = Flask(__name__)
db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

from app import routes, elastic

app.run
