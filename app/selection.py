#This file is where you can alter general parameters of which and how many articles should be selected for the news homepage. 


#Here you define the input that determines which articles are selected and how
#How many articles should be selected?
how_many = 10
#which topics should be selected
topics = "?"
#Among how many of the most recent articles should this selection be made?
among_sample = 100
#What is the selection logic (see recommender file)?
#recommender = random_selection

class newsselector():
	def __init__(self):
		self.how_many = how_many
		self.topics = topics
		self.among_sample = among_sample
#		self.recommender = recommender

#Function that selects n articles according to the previously defined input
	def select_articles(how_many, topics, among_sample, recommender):
		body = dict(size = among_sample, 
					sort=[{"date": {"order": "desc"}} #add topic selector
					],)
		articles = es.search(index="articles", body=body)['hits']['hits']
		selections = articles #"apply recommender here"
		return selections
