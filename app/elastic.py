from elasticsearch import Elasticsearch
from amcatclient import AmcatAPI

es = Elasticsearch()

amcat = AmcatAPI("https://vu.amcat.nl", "nickmattis", "Nimima&95")

es.indices.create("articles")

for article in amcat.get_articles(project=69, articleset=2564, start_date="2021-03-09", columns=("date", "title", "publisher", "url", "text", "author", "section")):
    es.create(index="article", id=article['id'], body=article)
