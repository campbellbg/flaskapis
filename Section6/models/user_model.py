import sqlite3
from Section6.db_setup import db_sql


# This class is just being used for the security script, which requires it. Use dictionaries for the API calls
class UserModel(db_sql.Model):

    __tablename__ = 'USERS' # Defining the table name

    # Defining the columns that map to the class constructor. Names are important, must match the database
    id = db_sql.Column(db_sql.Integer, primary_key = True)
    user_name = db_sql.Column(db_sql.String)
    user_pwd = db_sql.Column(db_sql.String)

    def __init__(self, _id, username, pwd):
        self.id = _id
        self.user_name = username
        self.user_pwd = pwd

    def json(self):
        return {'user_id': self.id, 'user_name': self.user_name, 'user_pwd': self.user_pwd}

    # Create a new user and return the object
    @classmethod
    def create_user(cls, username, pwd):

        the_user = cls.user_by_name(username)

        if not the_user:
            new_user = cls(None, username, pwd)
            # passing None will allow the auto-incrementing to work at db level
            db_sql.session.add(new_user)
            db_sql.session.commit()
            return new_user
        else:
            None

        '''
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

            return cls(1 if user_count[0] is None else user_count[0] + 1, username, pwd)

        else:
            return None
        '''

    '''
    ***************************************************************************************
    The below is used for the JWT creation and authentication, through the security script
    ***************************************************************************************
    '''

    # Get the user by name. To be used in the JW authenticate function
    @classmethod
    def user_by_name(cls, username): # , db_name):

        # Return the object constructed by the database row OR None if not available
        return UserModel.query.filter_by(user_name=username).first()

        '''
        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()

        result = my_cursor.execute('SELECT user_id, user_name, user_pwd FROM USERS WHERE user_name = ?',
                                   (username,)).fetchone() # fetches the first result. Only expecting one

        if result:
            return cls(result[0], result[1], result[2])
        else:
            return None
        '''


    # Get the user by ID. To be used in the JW identity function
    @classmethod
    def user_by_id(cls, userid): # , db_name):

        # Return the object constructed by the database row OR None if not available
        return UserModel.query.filter_by(id=userid).first()

        '''

        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()

        result = my_cursor.execute('SELECT user_id, user_name, user_pwd FROM USERS WHERE user_id = ?',
                                   (userid,)).fetchone() # fetches the first result. Only expecting one

        if result:
            return cls(result[0], result[1], result[2])
        else:
            return None
        '''