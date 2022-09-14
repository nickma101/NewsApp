"""
Handles the different routes that are necessary for the experiment: Backend API retrieval & database updates
(the frontend is determined by the react app)
- homepage to start the experiment
- recommendation page for the different article_sets from which users choose
- single article page where users can read and rate an article
- Finish page that re-directs users back to Qualtrics
"""
from flask import request, jsonify, redirect, url_for
from flask_cors import cross_origin
from app import app, db
from app import recommender
from .database import Exposures, Selections, Ratings, ArticleList
from datetime import datetime
import random


"""
Homepage
"""
@app.route('/')
def home():
    return "test"


"""
Recommendation page where article selection takes place
"""
@app.route('/recommendations', methods=["GET"])
@cross_origin()
def get_recommendations():
    user_id = request.args.get('user_id')
    experiment_id = recommender.select_article_set(user_id)
    timestamp = datetime.utcnow()
    exposures = list(Exposures.query.filter_by(user_id=user_id))
    no_of_previous_sets = len([exp.article_set_id for exp in exposures])
    nudge = ''
    article_id = request.args.get('article_id')
    rating = request.args.get('rating')
    if not experiment_id:
        raise Exception("No experiment id given")
    articles = recommender.get_articles(experiment_id, user_id)
    random.shuffle(articles)
    exposures = Exposures(article_set_id=experiment_id,
                                        user_id=user_id,
                                        timestamp=timestamp,
                                        nudge_id=nudge,
                                        exposure_id="{}/{}/{}".format(user_id, experiment_id, str(timestamp)))
    db.session.add(exposures)
    if no_of_previous_sets >0:
        ratings = Ratings(article_id=article_id,
                                    user_id=user_id,
                                    timestamp=timestamp,
                                    rating=rating,
                                    primary="{}/{}/{}".format(user_id, article_id, str(timestamp)))
        db.session.add(ratings)
    db.session.commit()
    return jsonify(articles)


"""
Article page where users can read and rate articles
"""
@app.route('/article', methods=["GET"])
@cross_origin()
def show_article():
    user_id = request.args.get('user_id')
    timestamp = datetime.utcnow()
    if not user_id:
        raise Exception("No user id given")
    article_id = request.args.get('article_id')
    if not article_id:
        raise Exception("No article id given")
    else:
        article_seen = Selections(article_id=article_id,
                                    user_id=user_id,
                                    timestamp=timestamp,
                                    primary="{}/{}/{}".format(user_id, article_id, str(timestamp)))
        db.session.add(article_seen)
        db.session.commit()
    return jsonify(recommender.get_article(user_id, article_id))


"""
Api to determine the next label to be displayed to a user
"""
@app.route('/label', methods=["GET"])
@cross_origin()
def select_label():
    user_id = request.args.get('user_id')
    timestamp = str(datetime.utcnow())
    if not user_id:
        raise Exception("No user id given")
    label = recommender.select_nudge(user_id)
    #nudge = Nudges(id=label, user_id=user_id, primary="{}/{}/{}".format(user_id, "label"+str(label), timestamp))
    #db.session.add(nudge)
    #db.session.commit()
    return jsonify(label)


"""
Api to determine whether users are finished
"""
@app.route('/finish', methods=["GET"])
@cross_origin()
def rounds_left():
    user_id = request.args.get('user_id')
    if not user_id:
        raise Exception("No user id given")
    exposures = list(Exposures.query.filter_by(user_id=user_id))
    seen_ids = {exp.article_set_id for exp in exposures}
    open_sets = set(recommender.experiment_ids) - seen_ids
    if not open_sets:
        print('no more sets')
        return jsonify(0)
    else:
        print('still more sets')
        return jsonify(1)


