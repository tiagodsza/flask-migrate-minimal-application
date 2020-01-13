from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:""@localhost/person"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

if __name__ == 'main':
    manager.run()