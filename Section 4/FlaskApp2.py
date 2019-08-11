# Section 4 of the course

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity  # These are the functions from the security.py file

my_app = Flask('Bryan App')
my_app.secret_key = 'bob'

my_api = Api(my_app)

# This creates a /auth end-point automatically
# A POST to this end-point will call the authenticate function
my_jwt = JWT(app=my_app, authentication_handler=authenticate, identity_handler=identity)

items = []


# Get the list of all Items
class Items(Resource):
    @jwt_required()
    def get(self):
        if not items:
            return {'items': None}, 404 # HTTP status not found
        else:
            return {'items': items}, 200


# For the Item Resource and gets and posts for this resource
class Item(Resource):

    @staticmethod
    def parse_args(*args):

        my_parser = reqparse.RequestParser()

        for i in args:
            my_parser.add_argument(name=i, required=True)

        return my_parser.parse_args()

    # HTTP GET
    def get(self, item_name):
        my_items = list(filter(lambda x: x['item_name'] == item_name, items))

        if not my_items:
            return {'error': 'An item of that name cannot be found'}, 404 # HTTP status not found
        else:
            return my_items, 200

    #HTTP POST
    def post(self, item_name):
        payload = request.get_json()
        new_item = {'item_name': item_name, 'item_price': payload['price']}

        if not list(filter(lambda x: x['item_name'] == item_name, items)):
            items.append(new_item)
            return new_item, 200
        else:
            return {'error': f'Item <{item_name}> could not be added'}, 400 # Bad Request

    #HTTP DELETE
    def delete(self, item_name):
        global items #This tells the function to use the global items variable, otherwise it thinks that it is being declared again locally

        pre_delete = len(items)
        items = list(filter(lambda x: x['item_name'] != item_name, items))

        if pre_delete != len(items):
            return {'message': 'item deleted'}, 200
        else:
            return {'error': 'no items to delete'}, 404

    #HTTP PUT
    def put(self, item_name):
        global items

        # Use the static method to get the price argument
        the_price = self.parse_args('item_price')

        new_item = {'item_name': item_name}
        new_item.update(the_price)

        # If it is in the list then remove it and add the new entry (like an update) otherwise append it
        if list(filter(lambda x: x['item_name'] == item_name, items)):
            print(items)
            items = list(filter(lambda x: x['item_name'] != item_name, items))
            items.append(new_item)
            print(items)
        else:
            items.append(new_item)

        return new_item


my_api.add_resource(Item, '/item/<string:item_name>')
my_api.add_resource(Items, '/items')

my_app.run(port=5555)
