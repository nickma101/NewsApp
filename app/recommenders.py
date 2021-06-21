from elasticsearch import Elasticsearch
from app import es
import random

'''Define how many articles should be selected'''
to_select = 10

class recommender():
	def __init__(self):
		self.to_select = to_select
	
	'''Selects a random sample of the input articles'''
	def random_selection(self, articles):
		articles = articles
		selections = random.sample(articles, to_select)
		return selections
