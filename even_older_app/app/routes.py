from app import app
from app.selection import newsselector
from elasticsearch import Elasticsearch
from app import db
from flask import request

newsselector = newsselector()

'''Homepage that displays news articles in json format'''
@app.route('/', methods= ['GET', 'POST'])
@app.route('/homepage', methods= ['GET', 'POST'])
def select_news():			
	return newsselector.make_recommendations()

'''Random API'''
@app.route('/random', methods= ['GET', 'POST'])
def select_random_news():			
	return newsselector.make_random_recommendations()
#to add: Post to user database

'''Recent API'''
@app.route('/recent', methods= ['GET', 'POST'])
def select_recent_news():			
	return newsselector.make_recent_recommendations()

@app.route("/users", methods=['POST'])
def create_user():
    """
    Create a new user. Request body should be a json with username, email, and password
    """
    data = request.get_json(force=True)
    if User.select().where(User.email == data['email']).exists():
        return bad_request("User {} already exists".format(data['email']))
    u = auth.create_user(username=data['username'], email=data['email'], password=data['password'])
    return jsonify({"id": u.id, "email": u.email}), HTTPStatus.CREATED

