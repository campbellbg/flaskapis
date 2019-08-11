# For section 5 of the course where we start adding SQLite capabilities
# A lot of this code has been copied from Section 4 and then changed to align with the SQLITE DB

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required

from security2 import authenticate, identity  # These are the functions from the security.py file
from db_users import create_user
from db_items import create_item, get_items, get_item, delete_item
from db_setup import setup_database, get_database

my_app = Flask('Bryan App')
my_app.secret_key = 'bob' # This would obviously not be done this way in Production code

my_api = Api(my_app)

# This creates a /auth end-point automatically
# A POST to this end-point will call the authenticate function
my_jwt = JWT(app=my_app, authentication_handler=authenticate, identity_handler=identity)

# Setup the database
setup_database(purge_records = True)
db_name = get_database()


# Get the list of all Items
class Items(Resource):
    @jwt_required()
    def get(self):
        all_items = get_items(db_name)

        if all_items:
            return {'items': all_items}, 200
        else:
            return {'items': None}, 404 # HTTP status not found


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

        my_item = get_item(item_name, db_name)

        if my_item:
            return my_item, 200 # HTTP success
        else:
            return {'error': 'An item of that name cannot be found'}, 404 # HTTP status not found

    # HTTP POST
    def post(self, item_name):

        item_price = self.parse_args('item_price')
        new_item = create_item(item_name, item_price['item_price'], db_name)

        if new_item:
            return new_item, 201  # HTTP created
        else:
            return {'error': f'item {item_name} was not able to be added'}, 400 # HTTP Bas Request

    # HTTP DELETE
    def delete(self, item_name):
        return delete_item(item_name, db_name), 200


class User(Resource):

    @staticmethod
    def parse_args(*args):
        my_parser = reqparse.RequestParser()

        for i in args:
            my_parser.add_argument(name=i, required=True)

        return my_parser.parse_args()

    # Creates a new user
    def post(self, user_name):
        user_pwd = self.parse_args('user_pwd')
        new_user = create_user(user_name, user_pwd['user_pwd'], db_name)

        if new_user:
            return new_user, 201 # HTTP created
        else:
            return {'error': f'user {user_name} was not able to be added'}, 400


my_api.add_resource(Item, '/item/<string:item_name>')
my_api.add_resource(Items, '/items')
my_api.add_resource(User, '/User/<string:user_name>')

my_app.run(port=5555)


