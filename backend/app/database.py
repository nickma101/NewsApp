"""
Defines database model for SQLAlchemy
"""


from app import db
from datetime import datetime


'''
DB for all articles that were selected (once a user selects an article it is added)
'''


class NewsSelected(db.Model):
    id = db.Column(db.Integer)
    title = db.Column(db.String(500))
    starttime = db.Column(db.DateTime, index=True)
    endtime = db.Column(db.DateTime, index=True)
    time_spent = db.Column(db.Interval)
    rating = db.Column(db.Numeric(2, 1), default=0)
    user_id = db.Column(db.Integer)
    Nudge = db.Column(db.String(50))
    primary = db.Column(db.String(500), primary_key=True)


'''
DB for article sets that were seen by users (once a user rates an article the set he selected it from is added)
'''


class ArticleSetsSeen(db.Model):
    id = db.Column(db.String(50))
    starttime = db.Column(db.DateTime, index=True)
    endtime = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer)
    primary = db.Column(db.String(500), primary_key=True)


'''
DB for all nudges that were displayed to a user
'''


class Nudges(db.Model):
    id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer)
    primary = db.Column(db.String(500), primary_key=True)
