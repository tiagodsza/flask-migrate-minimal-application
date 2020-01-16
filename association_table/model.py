from database import db

association_table = db.Table('association', db.Model.metadata,
                          db.Column('actor_id', db.Integer, db.ForeignKey('actor.id')),
                          db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)