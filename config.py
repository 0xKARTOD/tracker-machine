

from dotenv import load_dotenv
import os



icon = 'public/icon.png'
ethgas = 'public/ethgas.png'
ethereum = 'public/ethereum.png'
btcgas = 'public/btcgas.png'
bitcoin = 'public/bitcoin.png'



load_dotenv()
ApiKeyToken = os.getenv('APIKEY')
BASE_URL = 'https://api.etherscan.io/api?'

headerr = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}