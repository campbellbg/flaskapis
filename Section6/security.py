# This script looks at the use of JWT's in our APIs

from Section6.models.user_model import UserModel
from Section6.db_setup import get_database


# Check that the user exists and that the password is correct
def authenticate(username, password):
    user = UserModel.user_by_name(username) # , get_database())
    if user and user.user_pwd == password:
        return user


# This is what is called when the end-point is decorated as requiring the JWT
def identity(payload):
    user_id = payload['identity']  # The identity seems to come from the first 'key' of the serialised object

    #  It doesn't seem to matter what we return here
    return UserModel.user_by_id(user_id)  # , get_database())
