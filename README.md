# Tracker machine

Tracker machine is a tool that allows users to monitor and track the price of gas being used by transactions on the network and some cryptocurrecny prices. Gas trackers are particularly important for users who want to optimize the performance and cost-effectiveness of their transactions on the blockchain. Price trackers are useful for traders who want to follow the trend of price movementums.


## Plan

- [x] Add Ethereum L1 network gas and ETH price
- [x] Add Bitcoin network fees and BTC price
- [x] UI for up/down trends
- [x] Add automatic switch between metrics
- [x] Test for 10H
- [x] Optimize etherscan API data tracking
- [ ] Create an MacOS mini app
- [ ] Add more networks


## Interface

<img width="179" alt="image" src="https://github.com/0xKARTOD/tracker-machine/assets/100310858/e9253983-c994-4be6-b221-72f536cbd4c0">

<img width="276" alt="image" src="https://github.com/0xKARTOD/tracker-machine/assets/100310858/e2edb8bf-3088-4a54-aff4-16d95ce7b0d8">


## How to set up and run

1. Create `settings.txt` file
2. Put your etherscan API key there like `APIKEY = YOUR_API_KEY`
3. Run your app


> [!TIP]
> All the libraries that were used are in the ***requirements.txt*** file

Run via python:
```basg
python3 app.py
```
