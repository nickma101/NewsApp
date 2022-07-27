"""
Handles the articles that are displayed to users
- Retrieves articles from AmcatAPI with get articles
- Retrives user data and experimental settings
- Retrieves recommendation logic from recommender file
- creates recommendations for NewsApp API
"""

from app import db
from app.database import ArticleSetsSeen
from amcatclient import AmcatAPI
from app.experimental_settings import get_settings
import random

"""
1) Retriving articles (the stuff below will go into the config file)
"""
amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")
experiment_ids = ['article_set1', 'article_set2', 'article_set3', 'article_set4']

"""
Function that selects article set to be displayed to the user. 
Input: User_id
Output: Random selection from article_sets that were not yet seen by a user
"""


def select_article_set(user_id):
    exposures = list(ArticleSetsSeen.query.filter_by(user_id=user_id))
    seen_ids = {exp.id for exp in exposures}
    open_sets = set(experiment_ids) - seen_ids
    if not open_sets:
        return "that's it, no more open sets"
    else:
        experiment_id = random.choice(list(open_sets))
        return experiment_id


"""
Function that assigns nudging conditions in randomised order
Input: User_id
Output: Random selection of nudges yet to be displayed to the user
"""


def select_nudge(user_id):
    exposures = []
    nudge_ids = []
    # exposures = get_nudge_exposures(user_id) appends experiment ids to list
    conditions = []
    for e in nudge_ids:
        if e not in exposures:
            conditions.append(e)
    return random.choice(conditions)


"""
Function that retrieves articles from Amcat and returns them in randomised order
Input: experiment_id
Output: List of articles that matches the experiment id that is to be shown
"""


def get_articles(experiment_id, user_id):
    articles = []
    settings = get_settings(experiment_id)
    for article in amcat.get_articles(project=settings['project'],
                                      articleset=settings['amcat_article_set'],
                                      columns=settings['columns'],
                                      articleSet_int=settings['articleSet_int']):
        articles.append(article)
    random.shuffle(articles)
    return articles



"""
Function that retrieves most recent article set for a user. 
Input: User_id
Output: Random selection from article_sets that were not yet seen by a user
"""


def last_article_set(user_id):
    exposures = list(ArticleSetsSeen.query.filter_by(user_id=user_id))
    seen_ids = [exp.id for exp in exposures]
    last_one = seen_ids[-1]
    if not last_one:
        return "Something isn't right here"
    else:
        return last_one


""""
Function that retrieves a single article
"""


def get_article(user_id, article_id):
    user_id = user_id
    article_set = last_article_set(user_id)
    article_id = int(article_id)
    articles = []
    settings = get_settings(article_set)
    for article in amcat.get_articles(project=settings['project'],
                                      articleset=settings['amcat_article_set'],
                                      columns=settings['columns'],
                                      articleSet_int=settings['articleSet_int']):
        articles.append(article)
    article = [a for a in articles if a['id'] == article_id]
    if article:
        return article
    else:
        return "No article was found"
