#This script looks at the use of JWT's in our APIs

class User:
    def __init__(self, _id, user, pwd):
        self.id = _id
        self.user = user
        self.pwd = pwd


users = [User(1, 'Bryan', '123'), User(2, 'Kate', '123')]

name_map = {i.user:i for i in users}
id_map = {i.id:i for i in users}

# Check that the user exists and that the password is correct
def authenticate(username, password):
    user = name_map.get(username, None)
    if user: # and user.pwd == password:
        return user


#This is what is called when the end-point is decorated as requiring the JWT
def identity(payload):
    print(payload)
    user_id = payload['identity'] #  The identity seems to come from the first 'key' of the serialised object
    return id_map.get(user_id, None) #  It doesn't seem to matter what we return here
