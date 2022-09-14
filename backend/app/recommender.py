"""
Handles the articles that are displayed to users
- Retrieves article sets from AmcatAPI with get_articles()
- Retrieves single articles from AmcatAPI with get_article()
- Selects next nudge to be displayed to a user with select_nudge()
- Selects next article set to be displayed to a user with select_article_set()
"""

from app import db
from app.database import Exposures, Nudges
from amcatclient import AmcatAPI
from app.experimental_settings import get_settings
import random


"""
1) Retriving articles (the stuff below will go into the config file)
"""
amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")
experiment_ids = ['article_set1', 'article_set2', 'article_set3', 'article_set4']
nudge_ids = [1, 2, 3, 4]


"""
Function that selects article set to be displayed to the user. 
Input: User_id
Output: Random selection from article_sets that were not yet seen by a user
"""


def select_article_set(user_id):
    exposures = list(Exposures.query.filter_by(user_id=user_id))
    seen_ids = {exp.article_set_id for exp in exposures}
    open_sets = set(experiment_ids) - seen_ids
    if not open_sets:
        return 101
    else:
        experiment_id = random.choice(list(open_sets))
        return experiment_id


"""
Function that assigns nudging conditions in randomised order
Input: User_id
Output: Random selection of nudges yet to be displayed to the user
"""


def select_nudge(user_id):
    exposures = list(Nudges.query.filter_by(user_id=user_id))
    seen_nudges = {exp.id for exp in exposures}
    open_nudges = set(nudge_ids) - seen_nudges
    if not open_nudges:
        return "that's it, no more open nudges"
    else:
        nudge = random.choice(list(open_nudges))
        return nudge


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
    return articles


"""
Function that retrieves most recent article set for a user. 
Input: User_id
Output: The last article set that a user saw
"""


def last_article_set(user_id):
    exposures = list(Exposures.query.filter_by(user_id=user_id))
    seen_ids = [exp.article_set_id for exp in exposures]
    last_one = seen_ids[-1]
    if not last_one:
        return "Something isn't right here"
    else:
        return last_one


""""
Function that retrieves a single article
Input: User Id, Article Id
Output: A specific article
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
