"""
Recommenders: Handling custom end-points for article api's
Important: Customise to_select variable
"""
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from elastic import db, articledatabase

"""
Define the number of recent articles that will be initially retrieved before the
recommenders are applied
"""
to_select = 50

class MostRecentRecommender(Resource):
    #parse argument: how many articles to recommend
    parser = reqparse.RequestParser()
    parser.add_argument('number',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    #get request to retrieve x nost recent articles
    def get(self, number):
        data = Article.parser.parse_args()

        articles = db.search(index='articles', body={
            "size": data['number'],
            "sort":[{"date": {"order": "desc"}}]}).get('hits', {}).get('hits')
        recommendations = articles[:number]
        return jsonify(recommendations)

class RandomRecommender(Resource):
    #parse argument: how many articles to recommend
    parser = reqparse.RequestParser()
    parser.add_argument('number',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, number):
        data = Article.parser.parse_args()

        articles = db.search(index='articles', body={
            "size": data['number']})['hits']['hits']
        return articles



class CustomRecommender(Resource):
    pass
