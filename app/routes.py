from app import app
from app.selection import newsselector

#Homepage that displays news articles
@app.route('/', methods= ['GET', 'POST'])
@app.route('/homepage', methods= ['GET', 'POST'])
def select_news():
	return "This will become a newsapp!"
