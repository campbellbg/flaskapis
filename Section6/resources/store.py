# The store 'controller'. Contains the Class that extends the flask_restful Resource

from flask_restful import Resource, reqparse
from Section6.models.store_model import StoreModel


class Stores(Resource):

    @classmethod
    def get(cls):

        the_stores = StoreModel.get_stores()

        if the_stores:
            return [i.json() for i in the_stores]
        else:
            return {'message': 'no stores to return'}, 404 #HTTP not found


class Store(Resource):

    @classmethod
    def get(cls, store_name):

        the_store = StoreModel.get_store(store_name)

        if the_store:
            return the_store.json(), 201 #HTTP status create
        else:
            return {'error': f'Store {store_name} could not be found'}, 404 # HTTP not found

    @classmethod
    def post(cls, store_name):

        new_store = StoreModel.create_store(store_name)

        if new_store:
            return new_store.json(), 201 #HTTP status create
        else:
            return {'error': f'Store {store_name} could not be created'}, 400 # HTTP bad request

    @classmethod
    def delete(cls, store_name):

        the_store = StoreModel.delete_store(store_name)

        if the_store:
            return the_store.json(), 201  # HTTP status create
        else:
            return {'error': f'Store {store_name} could not be found'}, 404  # HTTP not found