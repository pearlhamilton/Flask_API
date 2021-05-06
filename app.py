from flask import Flask,request, jsonify
from controllers import dogs
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db 




app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dog.sqite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




CORS(app)



# class Dog(db.Model):
#     id = db.Column('dog_id', db.Integer, primary_key = True)
#     name = db.Column(db.String(20))
#     breed = db.Column(db.String(20))  
#     age = db.Column(db.Integer)

#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
    
#     def __repr__(self):
#         return '<Name %r>' % self.name
#     #     return '<Breed %r>' % self.breed
#     #     return '<Age %r>' % self.age




  





@app.route('/') 
def home(): # this will run when a GET request to '/' is mad
    # dogs_list = []

    
    # dogs = Dog.query.all()
    # for dog in dogs:
    #    dogs_list.append({"name":dog.name, "breed": dog.breed, "age":dog.age})
    # print(dogs_list)
    # return jsonify(dogs_list)
    return "hello"


@app.route('/api/dogs', methods=['GET', 'POST'])
def dogs_handler():
    fns= {
        'GET': dogs.index,
        'POST': dogs.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code


@app.route('/api/dogs/<int:dog_id>',methods=['GET', 'PATCH', 'PUT'] )
def dog_handler(dog_id):
    fns = {
        'GET': dogs.show,
        'PATCH': dogs.update,
        'PUT': dogs.update,
        'DELETE': dogs.destroy
    }
    resp, code = fns[request.method](request, dog_id)
    print(resp)
    return jsonify(resp), code
    


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()

db.init_app(app)





