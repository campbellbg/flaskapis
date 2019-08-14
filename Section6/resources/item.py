# The Item resources for my API

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from Section6.models.item_model import ItemModel
from Section6.db_setup import get_database

db_name = get_database()


# Get the list of all Items
class Items(Resource):
    #@jwt_required()
    def get(self):

        all_items = ItemModel.get_items()

        if all_items:
            # Use list comprehension to convert all list objects to dictionaries
            return {'items': [i.json() for i in ItemModel.get_items()]}, 200 # HTTP status ok
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

        my_item = ItemModel.get_item(item_name) # , db_name)

        if my_item:
            return my_item.json(), 200 # HTTP ok
        else:
            return {'error': 'An item of that name cannot be found'}, 404 # HTTP status not found

    # HTTP POST
    def post(self, item_name):

        item_args = self.parse_args('item_price', 'store_id')
        new_item = ItemModel.create_item(item_name, item_args['item_price'], item_args['store_id']) # , db_name)

        if new_item:
            return new_item.json(), 201  # HTTP created
        else:
            return {'error': f'item {item_name} was not able to be added'}, 400 # HTTP status Bad Request

    # HTTP DELETE
    def delete(self, item_name):

        deleted_item = ItemModel.delete_item(item_name)

        if deleted_item:
            return deleted_item.json(), 200
        else:
            return {'message': 'no item to be deleted'}, 404 # HTTP status not found
