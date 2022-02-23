"""
Recommenders: Handling custom end-points for article api's
"""
from flask_restful import Resource
from elastic import db, articledatabase

class CustomRecommender(Resource):
    pass

class MostRecentRecommender(Resource):
    pass

class RandomRecommender(Resource):
    pass
