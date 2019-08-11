#Looking at the packages / functions for working with SQlite from within python

import sqlite3

my_connection = sqlite3.Connection('mydb.db')

my_cursor = my_connection.cursor()

my_cursor.execute('CREATE TABLE IF NOT EXISTS items(item_id int,item_name text)')
my_cursor.execute('DELETE FROM ITEMS')

my_items = [(1, 'ITEM_1'), (2, 'ITEM_2'), (3, 'ITEM_3')]
my_cursor.executemany('INSERT INTO ITEMS VALUES(?, ?)', my_items)
my_connection.commit()

for i in my_cursor.execute('SELECT * FROM ITEMS'):
    print(i[0])

my_cursor.close()
my_connection.close()

