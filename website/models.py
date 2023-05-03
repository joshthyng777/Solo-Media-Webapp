from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #This is the foregin key that will reference the ID to another database column
    #for this isaiah it is saving the note for that specific user. Everytime we have a note we can see the user that created it with code on line 10

class Weight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight_data = db.Column(db.String(100))
    weight_lifted = db.Column(db.Integer)
    weight_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #This is the primary key that we referenced in line 10 user.id (user is class name)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #This sets a relationship between user and note
    weight = db.relationship('Weight')

    