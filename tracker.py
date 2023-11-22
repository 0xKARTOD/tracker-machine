import requests
from dotenv import load_dotenv
import os


load_dotenv()
ApiKeyToken = os.getenv('APIKEY')
BASE_URL = 'https://api.etherscan.io/api?'

def aggregate_data():
    return get_gas_price(), get_ethereum_price(), get_BTC_price(), get_BTC_gas()


def get_gas_price():

    url = f'{BASE_URL}module=gastracker&action=gasoracle&apikey={ApiKeyToken} '
    params = {}

    response = requests.get(url, params=params)
    data = response.json()
    
    return data['result']['SafeGasPrice']


def get_ethereum_price():

    url = f'{BASE_URL}module=stats&action=ethprice&apikey={ApiKeyToken}'
    params = {}

    response = requests.get(url, params=params)
    data = response.json()

    return float(data['result']['ethusd'])


def get_BTC_gas():

    url = 'https://mempool.space/api/v1/fees/recommended'
    params = {}

    response = requests.get(url, params=params)
    data = response.json()

    return data['hourFee']

def get_BTC_price():

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    params = {}

    response = requests.get(url, params=params)
    data = response.json()

    return float(data['bitcoin']['usd'])