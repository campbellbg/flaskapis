# The Item Class. Most of these methods are class methods, the don't really operate of an instance of an object
# rather that interact with the database and return ItemModel objects to the API methods, for presentation as JSON

#import sqlite3
from Section6.db_setup import db_sql


# Extend SQLAlchemy Model. This will tie the Class with the SQL Alchemy object
class ItemModel(db_sql.Model):

    __tablename__ = 'ITEMS' # Defining the table name

    # Defining the columns that map to the class constructor. Names are important, these must match the database
    item_id = db_sql.Column(db_sql.Integer, primary_key = True)
    item_name = db_sql.Column(db_sql.String)
    item_price = db_sql.Column(db_sql.Float)

    # Define the foreign key to the Stores table
    store_id = db_sql.Column(db_sql.Integer, db_sql.ForeignKey('STORES.store_id'))
    store_rel = db_sql.relationship('StoreModel')

    def __init__(self, _id, name, price, store_id):
        self.item_id = _id
        self.item_name = name
        self.item_price = price
        self.store_id = store_id

    def json(self):
        return {'item_id': self.item_id, 'item_name': self.item_name, 'item_price': self.item_price, 'store_id': self.store_id}

    # Create a new item and return the dictionary representation of it, once created successfully
    @classmethod
    def create_item(cls, item_name, item_price, store_id): #, db_name):

        # If the name doesn't already exist then add the row to the database using an object
        if not cls.get_item(item_name):
            new_item = cls(None, item_name, item_price, store_id)
            db_sql.session.add(new_item)
            db_sql.session.commit()
            return new_item
        else:
            return None

        '''
        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()

        item_count = my_cursor.execute('SELECT MAX(item_id), COUNT(CASE item_name WHEN ? THEN 1 ELSE NULL END) FROM ITEMS',
                                       (item_name,)).fetchone()

        if item_count[1] == 0:

            # NULL is required for the auto-incrementing column
            my_cursor.execute('INSERT INTO ITEMS VALUES(NULL,?,?)', (item_name, item_price))
            my_conn.commit()

            my_cursor.close()
            my_conn.close()

            # Return an object. The API method will convert to JSON
            return cls(1 if item_count[0] is None else item_count[0] + 1, item_name, item_price)

        else:
            return None
        '''


    # Get a specific item based on its name
    @classmethod
    def get_item(cls, item_name): #, db_name):

        # Will return an object of this class type as it maps result back to the constructor. Return None if no result
        return cls.query.filter_by(item_name = item_name).first()

        '''
        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()

        the_item = my_cursor.execute('SELECT item_id, item_name, item_price FROM ITEMS WHERE item_name = ?',
                                     (item_name,)).fetchone()

        if the_item:
            return cls(the_item[0], the_item[1], the_item[2])
        else:
            return None
        '''

    # Get all items from the database
    @classmethod
    def get_items(cls):  # db_name):

        #Will automatically return a list of objects. None if no items
        return ItemModel.query.all()

        '''
        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()
        all_items = []

        for i in my_cursor.execute('SELECT item_id, item_name, item_price FROM ITEMS'):
            all_items.append(cls(i[0], i[1], i[2]))

        return all_items
        '''

    # Delete an item based on its name
    @classmethod
    def delete_item(cls, item_name): # , db_name):

        the_item = cls.get_item(item_name)

        # If the name exists then delete the row to the database using an object
        if the_item:
            db_sql.session.delete(the_item)
            db_sql.session.commit()
            return the_item
        else:
            return None

        '''
        my_conn = sqlite3.Connection(db_name)
        my_cursor = my_conn.cursor()

        the_item = my_cursor.execute('DELETE FROM ITEMS WHERE item_name = ?',(item_name,))
        my_conn.commit()

        return cls(None, item_name, None)
        '''