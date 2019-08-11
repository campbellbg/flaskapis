# This script supports the Items interfaces with the database

import sqlite3


# Create a new item and return the dictionary representation of it, once created successfully
def create_item(item_name, item_price, db_name):

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

        # Return a dictionary. Makes the JSON return my flask_restful much more seamless
        return {'id': 1 if item_count[0] is None else item_count[0] + 1, 'item_name': item_name, 'item_price': item_price}

    else:
        return None


def get_item(item_name, db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    the_item = my_cursor.execute('SELECT item_id, item_name, item_price FROM ITEMS WHERE item_name = ?',
                                 (item_name,)).fetchone()

    if the_item:
        return {'item_id': the_item[0], 'item_name': the_item[1], 'item_price': the_item[2]}
    else:
        return None


# Get all items from the database
def get_items(db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()
    all_items = []

    for i in my_cursor.execute('SELECT item_id, item_name, item_price FROM ITEMS'):
        all_items.append({'id': i[0], 'item_name': i[1], 'item_price': i[2]})

    return all_items


def delete_item(item_name, db_name):

    my_conn = sqlite3.Connection(db_name)
    my_cursor = my_conn.cursor()

    the_item = my_cursor.execute('DELETE FROM ITEMS WHERE item_name = ?',(item_name,))
    my_conn.commit()

    return {'message': f'item {item_name} successfully deleted'}
