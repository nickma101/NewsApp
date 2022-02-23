"""
Database: Initialisation & methods
"""

from elasticsearch import Elasticsearch

#initialise elasticsearch
db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#retrieve articles
if db.indices.exists(index='articles') == True:
    articledatabase = db.search(index='articles')
else:
    db.indices.create("articles")
    articledatabase = db.search(index='articles')

"""
enables post requests for individual articles
requires a unique article id and any kind of metadate; e.g. in json format
"""
def upload_individual_article(id, metadata):
    try:
        db.index(index='articles', id=id, body=metadata)
    except:
        return {"message": "An error occurred uploading this article."}
