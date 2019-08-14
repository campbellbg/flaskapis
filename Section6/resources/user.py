# The user resource for my API

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from Section6.models.user_model import UserModel
from Section6.db_setup import get_database

db_name = get_database()


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
        new_user = UserModel.create_user(user_name, user_pwd['user_pwd']) # , db_name)

        if new_user:
            return new_user.json(), 201 # HTTP created
        else:
            return {'error': f'user {user_name} was not able to be added'}, 400