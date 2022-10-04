from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


newsapp = Flask(__name__)
db = SQLAlchemy(newsapp)
migrate = Migrate(newsapp, db)
newsapp.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
newsapp.secret_key = "youwillneverguess"


# to allow cross-domain access during development stage
cors = CORS(newsapp)

from . import routes

if __name__ == '__main__':
    newsapp.run(debug=True)  # important to mention debug=True
