# from __main__ import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class Dog(db.Model):
    id = db.Column('dog_id', db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    breed = db.Column(db.String(20))  
    age = db.Column(db.Integer)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def __repr__(self):
        return '<Name %r>' % self.name
    #     return '<Breed %r>' % self.breed
    #     return '<Age %r>' % self.age

