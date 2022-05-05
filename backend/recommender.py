"""
Handles the articles that are displayed to users
- Retrieves articles from AmcatAPI with get articles
- Retrives user data and experimental settings
- Retrieves recommendation logic from recommender file
- creates recommendations for NewsApp API
"""

from amcatclient import AmcatAPI
from experimental_settings import get_settings
import random

"""
1) Retriving articles (the stuff below will go into the config file)
"""
amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")
experiment_ids = [1, 2, 3, 4]

"""
Function that makes sure each article set is displayed consecutively 
"""
def select_article_set(user_id):
    exposures = []
    # exposures = get_article_set_exposures(user_id) appends experiment ids to list
    #article_set = len(exposures)+1
    #if article_set >5:
    #    link to qualtrics
    #else:
    #    return article_set

"""
Function that assigns nudging conditions in randomised order
"""
def select_nudge(user_id):
    exposures = []
    # exposures = get_nudge_exposures(user_id) appends experiment ids to list
    conditions = []
    for e in nudge_ids:
        if e not in exposures:
            conditions.append(e)
    return random.choice(conditions)

def get_articles(experiment_id, user_id):
    articles = []
    # experiment_id = select_article_set(user_id)
    settings = get_settings(experiment_id)
    for article in amcat.get_articles(project=settings['project'],
                                      articleset=settings['amcat_article_set'],
                                      start_date=settings['start_date'],
                                      columns=settings['columns']):
        articles.append(article)
    random.shuffle(articles)
    return articles