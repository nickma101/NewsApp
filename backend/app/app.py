from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app
app.secret_key = "youwillneverguess"


# to allow cross-domain access during development stage
cors = CORS(app)
app.config['CORS_Headers'] = 'Content-Type'


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
