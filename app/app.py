from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from recommender import recommendations


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"
api = Api(app)

class Recommendations(Resource):
    recommendations = recommendations
    def get(self):
        return recommendations

#api endpoints
#api.add_resource(Article, '/articles/<string:id>')
api.add_resource(recommendations, '/recommendations')


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
