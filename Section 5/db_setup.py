#Setup the database
import sqlite3

db_name = 'mydb.db'


# Create the database and its tables
def setup_database(purge_records):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    my_cursor.execute('CREATE TABLE IF NOT EXISTS ITEMS(item_id INTEGER PRIMARY KEY, item_name text, item_price float)')
    my_cursor.execute('CREATE TABLE IF NOT EXISTS USERS(user_id INTEGER PRIMARY KEY, user_name text, user_pwd text)')

    if purge_records:
        my_cursor.execute('DELETE FROM ITEMS')
        my_cursor.execute('DELETE FROM USERS')
        my_conn.commit()

    my_cursor.close()
    my_conn.close()


# Get the database details
def get_database():
    return db_name
