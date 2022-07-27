from flask import request, jsonify, redirect, url_for
from flask_cors import cross_origin
from app import app, db
from app import recommender
from .database import ArticleSetsSeen, NewsSelected


@app.route('/')
def home():
    return "test"


@app.route('/recommendations', methods=["GET"])
@cross_origin()
def get_recommendations():
    user_id = request.args.get('user_id')
    experiment_id = recommender.select_article_set(user_id)
    if not experiment_id:
        raise Exception("No experiment id given")
    article_sets_seen = ArticleSetsSeen(id=experiment_id, user_id=user_id)
    db.session.add(article_sets_seen)
    db.session.commit()
    return jsonify(recommender.get_articles(experiment_id, user_id))


@app.route('/article', methods=["GET"])
@cross_origin()
def show_article():
    user_id = request.args.get('user_id')
    if not user_id:
        raise Exception("No user id given")
    article_id = request.args.get('article_id')
    if not article_id:
        raise Exception("No article id given")
    return jsonify(recommender.get_article(user_id, article_id))
