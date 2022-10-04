"""
Handles the different routes that are necessary for the experiment: Backend API retrieval & database updates
(the frontend is determined by the React app)
- homepage to start the experiment
- recommendation page for the different article_sets from which users choose
- single article page where users can read and rate an article
- Finish page that re-directs users back to Qualtrics
"""
from flask import request, jsonify
from flask_cors import cross_origin
from .app import newsapp, db
from app import recommender
from .database import Exposures, Selections, Ratings, Articles, Nudges, User
from datetime import datetime
import random

"""
Homepage
"""

print("!!!", newsapp)

@newsapp.route('/')
def home():
    return "test"


"""
Recommendation page where article selection takes place
"""


@newsapp.route('/recommendations', methods=["GET"])
@cross_origin()
def get_recommendations():
    # handle users
    user_id = request.args.get('user_id')
    users = [user.user_id for user in User.query.all()]
    if int(user_id) not in users:
        user = User(user_id=user_id)
        db.session.add(user)
    # get other relevant parameters
    timestamp = datetime.utcnow()
    rated_article_id = request.args.get('article_id')
    rating = request.args.get('rating')
    if not rating:
        rating = 0
    # call recommender functions
    experiment_id = recommender.select_article_set(user_id)
    if not experiment_id:
        raise Exception("No experiment id given")
    nudge = recommender.select_nudge(user_id)
    nudge_id = int(nudge)
    nudge = Nudges(nudge_id=nudge_id,
                   user_id=user_id,
                   primary="{}/{}/{}".format(user_id,
                                             "label" + str(nudge_id),
                                             timestamp))
    db.session.add(nudge)
    # retrieve and log articles
    articles = recommender.get_articles(experiment_id)
    random.shuffle(articles)
    exposures = Exposures(article_set_id=experiment_id,
                          user_id=user_id,
                          timestamp_exposures=timestamp,
                          nudge_id=nudge_id,
                          exposure_id="{}/{}/{}".format(user_id,
                                                        experiment_id,
                                                        str(timestamp)))
    db.session.add(exposures)
    for article in articles:
        article_id = article['id']
        article_section = article['section']
        article_title = article['title']
        position = [i for i, d in enumerate(articles) if article_id in d.values()][0]
        user_id = user_id
        article_position = Articles(article_id=article_id,
                                    user_id=user_id,
                                    exposure_id="{}/{}/{}".format(user_id,
                                                                  experiment_id,
                                                                  str(timestamp)),
                                    section=article_section,
                                    title=article_title,
                                    position=position,
                                    nudge_id=nudge_id,
                                    primary="{}/{}/{}".format(user_id,
                                                              article_id,
                                                              experiment_id,
                                                              str(timestamp),
                                                              position))
        db.session.add(article_position)
    if int(rating) > 0:
        ratings = Ratings(article_id=rated_article_id,
                          user_id=user_id,
                          timestamp_ratings=timestamp,
                          rating=rating,
                          primary="{}/{}/{}".format(user_id,
                                                    article_id,
                                                    str(timestamp)))
        db.session.add(ratings)
        db.session.commit()
    db.session.commit()
    return jsonify(articles)


"""
Article page where users can read and rate articles
"""


@newsapp.route('/article', methods=["GET"])
@cross_origin()
def show_article():
    user_id = request.args.get('user_id')
    section = request.args.get('section')
    title = request.args.get('title')
    previous_nudging_condition = [nudge.nudge_id for nudge in Nudges.query.filter_by(user_id=user_id)][-1]
    nudge_id = 0
    if section == 'Current Affairs':
        nudge_id = previous_nudging_condition
    timestamp = datetime.utcnow()
    if not user_id:
        raise Exception("No user id given")
    article_id = request.args.get('article_id')
    print(article_id)
    if not article_id:
        raise Exception("No article id given")
    else:
        article_seen = Selections(article_id=article_id,
                                  title=title,
                                  section=section,
                                  previous_nudging_condition=previous_nudging_condition,
                                  nudge_id=nudge_id,
                                  user_id=user_id,
                                  timestamp_selections=timestamp,
                                  primary="{}/{}/{}".format(user_id,
                                                            article_id,
                                                            str(timestamp)))
        db.session.add(article_seen)
        db.session.commit()
    return jsonify(recommender.get_article(user_id, article_id))


"""
Api to determine the next label to be displayed to a user
"""


@newsapp.route('/label', methods=["GET"])
@cross_origin()
def select_label():
    user_id = request.args.get('user_id')
    if not user_id:
        raise Exception("No user id given")
    nudges = list(Nudges.query.filter_by(user_id=user_id))
    seen_nudges = [nudge.nudge_id for nudge in nudges]
    last_one = seen_nudges[-1]
    label = last_one
    return jsonify(label)


"""
Api to determine whether users are finished
"""


@newsapp.route('/finish', methods=["GET"])
@cross_origin()
def rounds_left():
    user_id = request.args.get('user_id')
    if not user_id:
        raise Exception("No user id given")
    exposures = list(Exposures.query.filter_by(user_id=user_id))
    seen_ids = {exp.article_set_id for exp in exposures}
    open_sets = set(recommender.experiment_ids) - seen_ids
    if not open_sets:
        return jsonify(0)
    else:
        return jsonify(1)


"""
Api to log last article rating
"""


@newsapp.route('/last_rating', methods=["GET"])
@cross_origin()
def log_last_rating():
    user_id = request.args.get('user_id')
    timestamp = datetime.utcnow()
    article_id = request.args.get('article_id')
    rating = request.args.get('rating')
    ratings = Ratings(article_id=article_id,
                      user_id=user_id,
                      timestamp_ratings=timestamp,
                      rating=rating,
                      primary="{}/{}/{}".format(user_id,
                                                article_id,
                                                str(timestamp)))
    db.session.add(ratings)
    db.session.commit()
    return 'does it matter?'
