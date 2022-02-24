"""
Database: Initialisation & methods
"""

from elasticsearch import Elasticsearch, helpers

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

#takes a list of articles and uploads them
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
