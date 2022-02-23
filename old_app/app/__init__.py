from flask import Flask
from elasticsearch import Elasticsearch

db = Elasticsearch([{'host': 'localhost', 'port': 9200}])
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    return app

from app import routes, elastic
