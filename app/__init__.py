from flask import Flask
from flask_login import LoginManager
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

login = LoginManager(app)

from app import routes, elastic

