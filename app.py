from flask import Flask,request, jsonify
from controllers import dogs

server = Flask(__name__)

@server.route('/') 
def home(): # this will run when a GET request to '/' is made
    return 'Hello from Flask!'


@server.route('/api/dogs', methods=['GET', 'POST'])
def dog_handler():
    fns= {
        'GET': dogs.index,
        'POST': dogs.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code




if __name__ == "__main__":
    server.run(debug=True)