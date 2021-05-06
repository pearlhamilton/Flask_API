dogs = [
    {'id': 1, 'name': 'Sadie', 'breed': 'Poodle', 'age': 3},
    {'id': 2, 'name': 'Pickle', 'breed': 'French Bulldog','age': 5},
    {'id': 3, 'name': 'Watson', 'breed': 'Boxer', 'age': 10}
]

def index(req):
    return [d for d in dogs], 200

def create(req):
    new_dog = req.get_json()
    new_dog['id'] = sorted([d['id'] for d in dogs])[-1] + 1
    dogs.append(new_dog)
    return new_dog, 201