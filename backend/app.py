from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import recommender
from database import User

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
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
def return_user():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
