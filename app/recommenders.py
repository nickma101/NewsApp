from elasticsearch import Elasticsearch
from app import es
import random
import json

'''How many articles should be selected'''
to_select = 10

class recommender():
	def __init__(self):
		self.to_select = to_select
	
	'''Selects a random sample of the input articles and returns a list of dictionaries with their meta-data in json format'''
	def random_selection(self, select_articles):
		articles = select_articles()
		recommendations = random.sample(articles, to_select)
		return json.dumps(recommendations)
	
	def most_recent(self, select_articles):
		articles = select_articles()
		recommendations = articles[:to_select]
		return json.dumps(recommendations)
