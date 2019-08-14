# The Store Class. Most of these methods are class methods, the don't really operate of an instance of an object
# rather that interact with the database and return ClassModel objects to the API methods, for presentation as JSON

from Section6.db_setup import db_sql


# Extend SQLAlchemy Model. This will tie the Class with the SQL Alchemy object
class StoreModel(db_sql.Model):

    __tablename__ = 'STORES' # Defining the table name

    # Defining the columns that map to the class constructor. Names are important, these must match the database
    store_id = db_sql.Column(db_sql.Integer, primary_key = True)
    store_name = db_sql.Column(db_sql.String)

    # Reference to the Primary Key. Allows the parent to get a list of children (a list of ItemModel objects)
    items = db_sql.relationship('ItemModel', lazy='dynamic')

    def __init__(self, _id, name):
        self.store_id = _id
        self.store_name = name

    def json(self):
        # list comprehension on the list of store objects
        return {'store_id': self.store_id, 'store_name': self.store_name, 'items': [i.json() for i in self.items]}

    # Create a new store and return the dictionary representation of it, once created successfully
    @classmethod
    def create_store(cls, store_name):

        # If the name doesn't already exist then add the row to the database using an object
        if not cls.get_store(store_name):
            new_store = cls(None, store_name)
            db_sql.session.add(new_store)
            db_sql.session.commit()
            return new_store
        else:
            return None

    # Get a specific store based on its name
    @classmethod
    def get_store(cls, store_name):

        # Will return an object of this class type as it maps result back to the constructor. Return None if no result
        return cls.query.filter_by(store_name = store_name).first()

    # Get all stores from the database
    @classmethod
    def get_stores(cls):  # db_name):

        # Will automatically return a list of objects. None if no stores
        return StoreModel.query.all()

    # Delete a store based on its name
    @classmethod
    def delete_store(cls, store_name):

        the_store = cls.get_store(store_name)

        # If the name exists then delete the row to the database using an object
        if the_store:
            db_sql.session.delete(the_store)
            db_sql.session.commit()
            return the_store
        else:
            return None
