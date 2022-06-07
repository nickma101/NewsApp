from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import recommender

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"

# to allow cross-domain access during development stage
cors = CORS(app)
app.config['CORS_Headers'] = 'Content-Type'


@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    experiment_id = request.args.get('experiment_id')
    user_id = request.args.get('user_id')
    #experiment_id = select_article_set(user_id)
    if not experiment_id:
        raise Exception("No experiment id given")
    return jsonify(recommender.get_articles(experiment_id, user_id))


@app.route("/users", methods=["GET", "PUT"])
def test():
    return "test"
#def add_user():

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
