from app import app
from app.selection import newsselector

@app.route('/', methods= ['GET'])
def select_news():
	return "This will become a newsapp!"
