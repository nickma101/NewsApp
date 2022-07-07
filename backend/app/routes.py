from flask import request, jsonify
from app import app, recommender
from app import db
from .database import ArticleSetsSeen, NewsSelected


@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    user_id = request.args.get('user_id')
    experiment_id = recommender.select_article_set(user_id)
    if not experiment_id:
        raise Exception("No experiment id given")
    article_sets_seen = ArticleSetsSeen(id=experiment_id, user_id=user_id)
    db.session.add(article_sets_seen)
    db.session.commit()
    return jsonify(recommender.get_articles(experiment_id, user_id))

@app.route("/article", methods=["GET"])
def get_article():
    user_id = request.args.get('user_id')
    article_id =
    articles = []
    for article in amcat.get_articles(project=settings['project'],
                                      columns=settings['columns']):
        articles.append(article)
    for article in articles:
        if article['id'] = article_id:
            return article
        else:
            return "Non existing article id"

@app.route("/users", methods=["GET", "PUT"])
def return_user():
    return 'test'
