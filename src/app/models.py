import datetime
from app import db


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(), unique=True, nullable=False)
    short_url = db.Column(db.String(), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url
        self.created_at = datetime.datetime.now()
