from backend.app.app import app, db
from backend.app.app import User


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
