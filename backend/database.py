from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    selected_news = db.relationship('News_sel', backref = 'user', lazy = 'dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.id)

'''
DB for all articles that were selected (once a user selects an article it is added)
'''
class NewsSelected(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500))
    starttime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    endtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    time_spent = db.Column(db.Interval)
    rating = db.Column(db.Numeric(2,1), default = 0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


'''
DB for article sets that were seen by users (once a user rates an article the set he selected it from is added)
'''
class ArticleSetsSeen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
