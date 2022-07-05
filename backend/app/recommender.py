from app import db
from app.database import ArticleSetsSeen

"""
Handles the articles that are displayed to users
- Retrieves articles from AmcatAPI with get articles
- Retrives user data and experimental settings
- Retrieves recommendation logic from recommender file
- creates recommendations for NewsApp API
"""

from amcatclient import AmcatAPI
from app.experimental_settings import get_settings
import random

"""
1) Retriving articles (the stuff below will go into the config file)
"""
amcat = AmcatAPI("https://vu.amcat.nl", "NickMattis")
experiment_ids = ['article_set1', 'article_set2', 'article_set3', 'article_set4']

"""
Function that makes sure each article set is displayed consecutively 
"""


def select_article_set(user_id):
    exposures = list(ArticleSetsSeen.query.filter_by(user_id = user_id))
    seen_ids = {exp.id for exp in exposures}
    open_sets = set(experiment_ids) - seen_ids
    if not open_sets:
        return "that's it, thanks"
    else:
        experiment_id = random.choice(list(open_sets))
        return experiment_id


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
    settings = get_settings(experiment_id)
    for article in amcat.get_articles(project=settings['project'],
                                      articleset=settings['amcat_article_set'],
                                      columns=settings['columns'],
                                      articleSet_int=settings['articleSet_int']):
        articles.append(article)
    random.shuffle(articles)
    return articles