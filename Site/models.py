from . import db
from flask_login import UserMixin
from datetime import datetime

class Notes(db.Model,UserMixin):
    __tablename__='notes'

    id= db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(350))   
    date = db.Column(db.DateTime(timezone=True),index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


class Users(db.Model,UserMixin):
    __tablename__ ='users'  

    id= db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50))
    firstname = db.Column(db.String(20),unique=True)  
    password = db.Column(db.String(20),unique=True)
    user_notes =db.relationship('Notes')
    