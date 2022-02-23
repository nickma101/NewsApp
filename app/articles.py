"""
Articles: Handling the article api endpoints
"""

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from elastic import db, articledatabase, upload_individual_article


#a class for individual articles
class Article(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, id):
        articles = db.search(index='articles')['hits']['hits']
        return {'article': next(filter(lambda x: x['_id'] == id, articles), None)}


    def post(self, id):
        if next(filter(lambda x: x['_id'] == id, articles), None):
            return {"message": "An item with id '{}' already exists.".format(id)}, 400

        data = Article.parser.parse_args()

        article = {'id': data['id'], 'metadata':{}}

        try:
            upload_individual_article(article['id'], article['metadata'])
        except:
            return {"message": "An error occurred uploading this article."}
        return article


    def delete(self, id):
        db.delete(index = "articles", id = id)
        return {'message': 'Article deleted'}


    def put(self, name):
        data = Article.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        article = next(filter(lambda x: x['name'] == id, articles), None)
        if article is None:
            article = {'id': id, 'title': data['title'], 'teaser': data['teaser'],
                'text': data['text']}
            articles.append(article)
        else:
            article.update(data)
        return article

class ArticleList(Resource):
    def get(self):
        return {'articleList': articles}
