from backend.app.app import app, db
from backend.app.app import User, Nudges, Exposures, Selections, Ratings, Articles


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
