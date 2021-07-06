from app import app
from app.selection import newsselector
from elasticsearch import Elasticsearch
from app import es

newsselector = newsselector()

'''Homepage that displays news articles in json format'''
@app.route('/', methods= ['GET', 'POST'])
@app.route('/homepage', methods= ['GET', 'POST'])
def select_news():			
	return newsselector.make_recommendations()

'''Random API'''
@app.route('/random', methods= ['GET', 'POST'])
def select_random_news():			
	return newsselector.make_random_recommendations()
#to add: Post to user database

'''Recent API'''
@app.route('/recent', methods= ['GET', 'POST'])
def select_recent_news():			
	return newsselector.make_recent_recommendations()
#to add: Post to user db
