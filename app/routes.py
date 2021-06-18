from app import app
from app.selection import newsselector
from elasticsearch import Elasticsearch
from app import es

newsselector = newsselector()

#Homepage that displays news articles
@app.route('/', methods= ['GET', 'POST'])
@app.route('/homepage', methods= ['GET', 'POST'])
def select_news():		
	return es.search(index='articles', body={'query': {'match': {'text': 'a'}}})
	
	#return newsselector.test()

	#return "This will become a newsapp!"
