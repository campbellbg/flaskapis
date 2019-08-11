#This script looks at the use of JWT's in our APIs

import db_users
import db_setup


# Check that the user exists and that the password is correct
def authenticate(username, password):
    user = db_users.user_by_name(username, db_setup.get_database())
    if user and user.user_pwd == password:
        return user


# This is what is called when the end-point is decorated as requiring the JWT
def identity(payload):
    user_id = payload['identity'] #  The identity seems to come from the first 'key' of the serialised object
    return db_users.user_by_id(user_id, db_setup.get_database()) #  It doesn't seem to matter what we return here
