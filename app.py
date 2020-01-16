from datetime import datetime

from flask_migrate import Migrate
from movie.model import Movie
from actor.model import Actor
from database import db, app

migrate = Migrate(app, db)

if __name__ == 'main':
    app.run()

#Comente a linha abaixo antes de fazer o migrate
# leonardo = Actor(name="Leonardo de Caprio")
# mathew = Actor(name="matthew mcconaughey")
#
# db.session.add(leonardo)
# db.session.commit()