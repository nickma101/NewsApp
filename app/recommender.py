"""
Recommenders: Handling custom end-points for article api's
"""
from flask_restful import Resource, Api, reqparse
from flask import jsonify
from elastic import db, articledatabase

"""
Define the number of recent articles that will be retrieved with the variable below
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
    pass

class CustomRecommender(Resource):
    pass
