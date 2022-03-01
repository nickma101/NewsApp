from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from articles import Article, ArticleList
from recommender import CustomRecommender, MostRecentRecommender, RandomRecommender


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"
api = Api(app)

#api endpoints for articles, A list of all articles, and various Recommenders

#takes get & post requests
api.add_resource(Article, '/articles/<string:id>')
api.add_resource(ArticleList, '/articles')

#only takes get requests; recommender logic is defines in recommender.py
api.add_resource(CustomRecommender, '/custom')
api.add_resource(MostRecentRecommender, '/recent')
api.add_resource(RandomRecommender, '/random')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
