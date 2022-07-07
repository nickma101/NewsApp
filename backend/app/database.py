"""
Define database model for SQLAlchemy
"""


from app import db
from datetime import datetime


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
    id = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow, primary_key = True)
    user_id = db.Column(db.Integer)