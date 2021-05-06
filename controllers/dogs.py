from werkzeug.exceptions import BadRequest
from models import Dog



# dogs = [
#     {'id': 1, 'name': 'Sadie', 'breed': 'Poodle', 'age': 3},
#     {'id': 2, 'name': 'Pickle', 'breed': 'French Bulldog','age': 5},
#     {'id': 3, 'name': 'Watson', 'breed': 'Boxer', 'age': 10}
# ]

def index(req):
    dogs_list = []


    dogs = Dog.query.all()
    for dog in dogs:
        dogs_list.append({"name":dog.name, "breed": dog.breed, "age":dog.age})
    print(dogs_list)
    return dogs_list, 200

def create(req):
    new_dog = req.get_json()
    new_dog['id'] = sorted([d['id'] for d in dogs])[-1] + 1
    dogs.append(new_dog)
    return new_dog, 201

def show(req, dog_id):
    return find_by_id(dog_id), 201

def update(req, dog_id):
    new_data = req.get_json()
    dog = find_by_id(dog_id)
    for key, val in new_data.items():
        dog[key] = val
    return dog, 200

def destroy(req, dog_id):
    dog_to_destory = find_by_id(dog_id)
    dogs.remove(dog_to_destory)
    return dog,204





# helper functions

def find_by_id(uid):
    try:
        return next(dog for dog in dogs if dog['id'] == uid)
    except:
        raise BadRequest(f"We don't have that dog with id {uid}!")
