from app import db
from elasticsearch import Elasticsearch

# Functions for working with the database (e.g. adding users, articles, ...)
# 3 key databases in ES: articles, users, experiments

#add articles using a targetfile and defining an experiment
def add_articles(filename, epxeriment):
    articles = pd.read_csv(filename)
    for article in articles:
        db.index(index="articles", id=article['id'])

#import requests
#db = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#x = requests.get("http://localhost:9200/articles/_mapping")
#print(x.text)
