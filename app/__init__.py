from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from elasticsearch import Elasticsearch

app = Flask(__name__)
db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

login = LoginManager(app)

from app import routes, elastic

app.run
