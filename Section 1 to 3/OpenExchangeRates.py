#Using the Python requests package to get NZ to AUS rates

'''
NOTES:
1) Needed to register for a free App ID. 1000 requests per month
2) Free API's do not allow for the base currency to be changed. It is set to USD
'''

import requests
from flask import Flask

my_app = Flask('ExchangeRate')

@my_app.route('/')
def get_nz_aud_rate():

    app_id = 'b9d07c9863f84a88b77bc07f7d878a37'
    endpoint = 'https://openexchangerates.org/api/latest.json'

    the_response = requests.get(f'{endpoint}?app_id={app_id}')
    all_rates = the_response.json()['rates']

    #Get the AUS and NZD rates
    return f'$1 AUD is equal to ${all_rates["NZD"] / all_rates["AUD"]} NZD'


my_app.run(port=5555)


