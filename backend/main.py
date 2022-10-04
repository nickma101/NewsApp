from app.app import newsapp, db
from app.database import User, Nudges, Exposures, Selections, Ratings, Articles


@newsapp.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
