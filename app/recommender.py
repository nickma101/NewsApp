"""
Handles the articles that are displayed to users
- Retrieves articles from AmcatAPI
- Retrives user data and experimental settings
- Retrieves recommendation logic from recommender file
- creates recommendations for NewsApp API
"""

from amcatclient import AmcatAPI
from experimental_settings import experimental_parameters

"""
1) Retriving articles (the stuff below will go into the config file)
"""

amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")

def retrieve_articles(parameters):
    parameters = parameters
    articles = []
    for article in amcat.get_articles(project = parameters['project'],
    articleset=parameters['articleset'],
    start_date=parameters['start_date'],
    columns=parameters['columns']):
        articles.append(article)
    return articles

#or article in amcat.get_articles(project=69, articleset=2564, start_date="2021-03-09", columns=("date", "title", "publisher", "url", "text", "author", "section")):

"""
2) Retrieve user data and experimental settings
"""

"""
Make recommendations
"""
recommendations = retrieve_articles(experimental_parameters)
