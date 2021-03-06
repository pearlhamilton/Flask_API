from flask import Flask,request, jsonify
from controllers import dogs
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/') 
def home(): # this will run when a GET request to '/' is made
    return 'Hello from Flask!'


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