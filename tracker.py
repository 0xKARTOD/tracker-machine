import requests
from dotenv import load_dotenv
import os
from threading import Thread
from queue import Queue


load_dotenv()
ApiKeyToken = os.getenv('APIKEY')
BASE_URL = 'https://api.etherscan.io/api?'

headerr = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

def wrapper(func, queue):
    queue.put(func())

def aggregate_data():

    funcs = [get_gas_price, get_ethereum_price, get_BTC_price, get_BTC_gas]
    q = []
    _return = []
    for i in range(len(funcs)):
        q.append(Queue())
        Thread(target = wrapper, args=(funcs[i], q[i])).start() 

    for i in range(len(q)):
        _return.append(q[i].get())

    return _return


def get_gas_price():

    url = f'{BASE_URL}module=gastracker&action=gasoracle&apikey={ApiKeyToken} '

    response = requests.get(url, headers = headerr)
    data = response.json()
    
    return data['result']['SafeGasPrice']


def get_ethereum_price():

    url = f'{BASE_URL}module=stats&action=ethprice&apikey={ApiKeyToken}'

    response = requests.get(url, headers = headerr)
    data = response.json()

    return float(data['result']['ethusd'])


def get_BTC_gas():

    url = 'https://mempool.space/api/v1/fees/recommended'

    response = requests.get(url, headers = headerr)
    data = response.json()

    return data['hourFee']

def get_BTC_price():

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

    response = requests.get(url, headers = headerr)
    data = response.json()

    return float(data['bitcoin']['usd'])