from database import db
from association_table.model import association_table

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    actors = db.relationship("Actor", secondary=association_table, back_populates="movies")