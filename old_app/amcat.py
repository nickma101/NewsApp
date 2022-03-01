"""
File to upload Json files from Amcat into the article Database
Just edit the name of the json_file and run from terminal
"""

from  elasticsearch import Elasticsearch
import json

db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

json_file = 'data.json'

#takes a json file and indexes articles into elasticsearch database. body can be customised
def upload_amcat_articles(json_file):
    f = open(json_file)
    data = json.load(f)['results']
    #include relevant metadata below
    for e in data:
        id = e['id']
        title = e['title']
        date = e['date']
        db.index(index='articles', id=id, body= {"title": title, "date": date})

upload_amcat_articles(json_file)
