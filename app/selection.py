'''This file is where you can alter general parameters of which and how many articles should be selected for the news homepage.'''

from elasticsearch import Elasticsearch
from app import es
from app.recommenders import recommender

'''Here you define the input that determines which articles are selected and how'''

'''How many of the most recent articles should be selected?'''
how_many = 20

'''which topics should be selected'''
topics = "politiek binnenland"

'''For number of articles to select see recommender file'''

'''What is the selection logic (see recommender file)? Add the preferred method in line 38 (default: random_selection)'''

recommender = recommender()

class newsselector():
	def __init__(self):
		self.how_many = how_many
		self.topics = topics
		self.recommender = recommender
	'''Function that selects n articles according to the previously defined input'''	
	'''Returns list of dictionaries with meta-info per article'''	
	def select_articles(self):
		selected_articles = es.search(index='articles', body={
			"size": how_many,
			"sort":[{"date": {"order": "desc"}}],
			'query': {'match': {'section': {"query": topics, "operator": "or"}}}})
		nested_articles = selected_articles.get('hits', {}).get('hits')
		articles = [e['_source'] for e in nested_articles]
		return articles
		
	def make_recommendations(self):
		return recommender.random_selection(self.select_articles)
