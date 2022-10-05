"""
Defines database model for SQLAlchemy
"""


from . import db
from datetime import datetime
'''
DB for all nudges that were displayed to a user
'''


class Nudges(db.Model):
    nudge_id = db.Column(db.Integer)
    timestamp_nudges = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    primary = db.Column(db.String(500), primary_key=True)


'''
DB for all article sets that were displayed to a user
'''


class Exposures(db.Model):
    article_set_id = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    timestamp_exposures = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    exposure_id = db.Column(db.String(500), primary_key=True)
    nudge_id = db.Column(db.Integer)


'''
DB for all articles that users selected
'''


class Selections(db.Model):
    article_id = db.Column(db.String(50))
    title = db.Column(db.String(50))
    section = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    timestamp_selections = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    primary = db.Column(db.String(500), primary_key=True)
    nudge_id = db.Column(db.Integer)
    previous_nudging_condition = db.Column(db.Integer)


'''
DB for all articles that users rated
'''


class Ratings(db.Model):
    article_id = db.Column(db.String(50))
    rating = db.Column(db.Numeric(2, 1), default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    timestamp_ratings = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    primary = db.Column(db.String(500), primary_key=True)


'''
DB for all individual articles that users were exposed to including positioning
'''


class Articles(db.Model):
    exposure_id = db.Column(db.String(500), db.ForeignKey('exposures.exposure_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    article_id = db.Column(db.String(50))
    nudge_id = db.Column(db.Integer)
    position = db.Column(db.Integer)
    title = db.Column(db.String(50))
    section = db.Column(db.String(50))
    primary = db.Column(db.String(500), primary_key=True)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    qualtrics_id = db.Column(db.String(500))
    overall_time = timestamp_ratings = db.Column(db.DateTime, index=True)  # not functioning atm
