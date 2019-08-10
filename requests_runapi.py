'''
Using the python requests package to interact with the API's programatically rather than using Postman. I actually
prefer this
'''

import requests

endpoint_item = 'http://127.0.0.1:5555/item/'
endpoint_items = 'http://127.0.0.1:5555/items'
endpoint_auth = 'http://127.0.0.1:5555/auth'
headers_content = {"Content-Type": "application/json"}

# Add a product
def add_product(item_name, item_price):

    the_url = endpoint_item + item_name
    the_payload = '{"price":"' + item_price + '"}'

    response = requests.post(url=the_url, data=the_payload, headers=headers_content)
    print(response.json())

# Add or Update product
def put_product(item_name, item_price):

    the_url = endpoint_item + item_name
    the_payload = '{"item_rice":"' + item_price + '"}'

    response = requests.put(url=the_url, data=the_payload, headers=headers_content)
    print(response.json())


def list_items(my_jwt):

    the_url = endpoint_items
    the_headers = {'Authorization': 'JWT ' + my_jwt}

    response = requests.get(url=the_url, data=None, headers=the_headers)
    print(response.json())


def get_jwt(username, password):

    the_url = endpoint_auth
    the_payload = '{"username":"' + username + '", "password":"' + password + '"}'

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url=the_url, data=the_payload, headers=headers_content)
    return response.json()['access_token']


session_jwt = get_jwt('Bryan', '123')

add_product('Product 1', '1.23')
add_product('Product 2', '2.55')
put_product('Product 1', '1.23')
list_items(session_jwt)