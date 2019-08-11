# This script supports the Users interfaces with the database AND the security script

import sqlite3


# This class is just being used for the security script, which requires it. Use dictionaries for the API calls
class User:
    def __init__(self, _id, username, pwd):
        self.id = _id
        self.user_name = username
        self.user_pwd = pwd


# Create a new user and return the object
def create_user(username, pwd, db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    user_count = my_cursor.execute('SELECT MAX(user_id), COUNT(CASE user_name WHEN ? THEN 1 ELSE NULL END) FROM USERS',
                                   (username,)).fetchone()

    if user_count[1] == 0:

        # NULL is required for the auto-incrementing column
        my_cursor.execute('INSERT INTO USERS VALUES(NULL,?,?)', (username, pwd))
        my_conn.commit()

        my_cursor.close()
        my_conn.close()

        # Return a dictionary representation of the user
        return {'user_id': 1 if user_count[0] is None else user_count[0] + 1, 'user_name': username, 'user_pwd': pwd}

    else:
        return None

'''
***************************************************************************************
The below is used for the JWT creation and authentication, through the security script
***************************************************************************************
'''


# Get the user by name. To be used in the JW authenticate function
def user_by_name(username, db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    result = my_cursor.execute('SELECT user_id, user_name, user_pwd FROM USERS WHERE user_name = ?', (username,)).fetchone() # fetches the first result. Only expecting one

    if result:
        return User(result[0], result[1], result[2])
    else:
        return None


# Get the user by ID. To be used in the JW identity function
def user_by_id(userid, db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    result = my_cursor.execute('SELECT user_id, user_name, user_pwd FROM USERS WHERE user_id = ?', (userid,)).fetchone() # fetches the first result. Only expecting one

    if result:
        return User(result[0], result[1], result[2])
    else:
        return None
