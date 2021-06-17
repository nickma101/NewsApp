from app import app
from app.selection import newsselector

#Homepage that displays news articles
@app.route('/', methods= ['GET', 'POST'])
@app.route('/homepage', methods= ['GET', 'POST'])
def select_news():
	return "This will become a newsapp!"

#User registration, log-in and log-out
@app.route('/register', methods=['GET', 'POST'])
	
@app.route('/login', methods = ['GET', 'POST'])

@app.route('/logout')

#User profile with statistics -> to be added at a later stage
@app.route('/profile')
