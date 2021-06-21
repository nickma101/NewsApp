'''This file is where you can alter general parameters of which and how many articles should be selected for the news homepage.'''

from elasticsearch import Elasticsearch
from app import es
from app.recommenders import recommender
import random
import json

'''Here you define the input that determines which articles are selected and how'''

'''How many of the most recent articles should be selected?'''
how_many = 20

'''which topics should be selected'''
topics = "politiek binnenland"

'''What is the selection logic (see recommender file)?'''
recommender = recommender()

class newsselector():
	def __init__(self):
		self.how_many = how_many
		self.topics = topics
		self.recommender = recommender
	'''Function that selects n articles according to the previously defined input'''	
	'''Returns JSON object'''	
	def select_articles(self):
		selected_articles = es.search(index='articles', body={
			"size": how_many,
			"sort":[{"date": {"order": "desc"}}],
			'query': {'match': {'section': {"query": topics, "operator": "or"}}}})
		return selected_articles
	
	def make_recommendations(self):
		articles = self.select_articles()
		return articles
		#articles = artlices.get('hits',{}).get('hits',[""])
		#return random.sample(artlices, 10)
		#		articles = es.search(index="articles", body=body)['hits']['hits']
