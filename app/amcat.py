from  elasticsearch import Elasticsearch
import json

db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

json_file = 'data.json'

def upload_amcat_articles(json_file):
    f = open(json_file)
    data = json.load(f)['results']
    for e in data:
        id = e['id']
        title = e['title']
        date = e['date']
        db.index(index='articles', id=id, body= {"title": title, "date": date})

upload_amcat_articles(json_file)
