"""
Database: Initialisation & methods
"""

from elasticsearch import Elasticsearch, helpers

#initialise elasticsearch
db = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#retrieve articles or create index if non-existent
if db.indices.exists(index='articles') == True:
    articledatabase = db.search(index='articles')
else:
    db.indices.create("articles")
    articledatabase = db.search(index='articles')

#retrieve experiments or create index if non-existent
if db.indices.exists(index='experiments') == True:
    articledatabase = db.search(index='experiments')
else:
    db.indices.create("experiments")
    articledatabase = db.search(index='experiments')


"""
function that enables post requests for individual articles
requires a unique article id and metadata in json format
Metatdata must include: title, teaser, text, author, source, date, and experiment_id
"""
def upload_individual_article(id, metadata):
    try:
        doc = {
            'title': metadata['title'],
            'teaser': metadata['teaser'],
            'text': metadata['text'],
            'author': metadata['author'],
            'source': metadata['source'],
            'date': metadata['date'],
            'experiment_id': metadata['experiment_id']
        }
        db.index(index='articles', id=id, body=doc)
    except:
        return {"message": "An error occurred uploading this article."}

"""
function that ...
"""
def upload_articles(list_of_articles):
    for a in list_of_articles:
        id = a['id']
        metadata = a['metadata']
        try:
            db.index(index='articles', id=id, body=metadata)
        except:
            return {"message": "An error occurred uploading these articles."}


#not tested
#from: https://kb.objectrocket.com/elasticsearch/how-to-use-python-helpers-to-bulk-load-data-into-an-elasticsearch-index
def bulk_upload(json_file, _index, doc_type):

    def bulk_json_data(json_file, _index, doc_type):
        json_list = get_data_from_file(json_file)
        for doc in json_list:
            # use a `yield` generator so that the data isn't loaded into memory

            if '{"index"' not in doc:
                yield {
                    "_index": _index,
                    "_type": doc_type,
                    "_id": uuid.uuid4(),
                    "_source": doc
                }
    try:
        # make the bulk call, and get a response
        response = helpers.bulk(elastic, bulk_json_data("people.json", "employees", "people"))
        print ("\nRESPONSE:", response)
    except Exception as e:
        print("\nERROR:", e)
