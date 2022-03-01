"""
Handles the articles that are displayed to users
- Retrieves articles from AmcatAPI
- Retrives user data and experimental settings
- Retrieves recommendation logic from recommender file
- creates recommendations for NewsApp API
"""

from amcatclient import AmcatAPI
from experimental_settings import get_settings
import json

"""
1) Retriving articles (the stuff below will go into the config file)
"""

amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")

def get_articles(experiment_id, user_id):
    settings = get_settings(experiment_id)
    articles = []
    for article in amcat.get_articles(project = settings['project'],
            articleset=settings['articleset'],
            start_date=settings['start_date'],
            columns=settings['columns']):
        articles.append(article)
    return articles


"""
2) Retrieve user data and experimental settings
"""
