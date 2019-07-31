# The first Flask App for the course

# flask is the package Flask is the class
from flask import Flask, jsonify, request, render_template


# Basic class for my Stores
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_items(self, item):
        self.items.append(item)


# Very basic class for an Item. Saves me creating a dictionary
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# A dummy store for testing purposes
my_stores = []
test_store = Store('Tester')
test_store.add_items(Item('Tester', 1.99))
my_stores.append(test_store)
my_stores.append(test_store)

# Create the app instance
my_app = Flask('StoreApp')


#Root Route
@my_app.route('/')
def home_page():
    return render_template('index.html')


# POST /store data: {name:}
@my_app.route('/store', methods=['POST'])
def post_store():
    the_request = request.get_json() # Takes the JSON response and turns it into a python dictionary

    if 'store_name' in the_request:
        new_store = Store(name=the_request['store_name'])

        # Add the store
        my_stores.append(new_store)

        return jsonify({'store_name': new_store.name})
    else:
        return jsonify({'error': 'incorrect parameters have been passed'})


# GET /store/<string:name>
@my_app.route('/store/<string:store_name>', methods=['GET'])
def get_store(store_name):

    the_store = [{'store_name': i.name} for i in my_stores if i.name == store_name]

    if not the_store: # if the list is empty
        return jsonify({'error': 'store not successfully found'})
    elif len(the_store[0]) > 1:
        return jsonify({'error': 'more than one store found'})
    else:
        return jsonify(the_store[0])


# GET /store
@my_app.route('/store', methods=['GET'])
def get_stores():

    # List comprehension makes this code super succinct. Pretty cool
    all_stores = [{'store_name': i.name} for i in my_stores]

    return jsonify({'stores': all_stores})  # pass the list in with a single dictionary key so that jsonify can accept it


# POST /store/<string:name>/item {item_name:, item_price:}
@my_app.route('/store/<string:store_name>/item', methods=['POST'])
def post_item(store_name):
    the_request = request.get_json()

    # ensure that the expected names were passed in the JSON
    if 'item_name' in the_request and 'item_price' in the_request:
        for i in my_stores:
            if i.name == store_name:
                new_item = Item(name=the_request['item_name'], price=the_request['item_price'])
                i.add_items(new_item)
                return jsonify({'item_name': new_item.name})

    return jsonify({'Error':'Item could not be added'})  # Will only get to this return if the store is not found OR there is incorrect JSON input


# GET /store/<string:name>/item
@my_app.route('/store/<string:store_name>/item', methods=['GET'])
def get_items(store_name):

    the_store = [i for i in my_stores if i.name == store_name]

    if not(not the_store): # if it is not empty
        the_items = [{'item_name': i.name} for i in the_store[0].items]
        return jsonify({'items': the_items})
    else:
        return jsonify({'Error': 'store not successfully found '})


my_app.run(port=5000)