from database import db
from association_table.model import association_table

class Actor(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    time = db.Column(db.DateTime())
    movies = db.relationship("Movie", secondary=association_table, back_populates="actors")
