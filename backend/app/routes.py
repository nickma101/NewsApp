from flask import request, jsonify
from app import app, recommender

@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    experiment_id = request.args.get('experiment_id')
    user_id = request.args.get('user_id')
    #experiment_id = select_article_set(user_id)
    if not experiment_id:
        raise Exception("No experiment id given")
    return jsonify(recommender.get_articles(experiment_id, user_id))


@app.route("/users", methods=["GET", "PUT"])
def return_user():
    return 'test'