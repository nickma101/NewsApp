from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from articles import Article, ArticleList
#from security import authenticate, identity

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"
api = Api(app)

api.add_resource(Article, '/articles/<string:id>')
api.add_resource(ArticleList, '/articles')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
