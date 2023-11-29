import rumps

from tracker import *

from config import *

class TrackerApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Tracker",
            "gas": "Show ETH Gas",
            "eth": "Show ETH price",
            "btc": "Show BTC price",
            "btcgas": "Show BTC Gas",
            "scroll": "Data scrolling",
            "break_message": "Gas is high"
        }
        self.timeout = 60
        self.flags_list = ['GAS', 'ETH', 'BTCGAS', 'BTC']
        self.i = 0
        self.app = rumps.App(self.config["app_name"])
        self.gas_button = rumps.MenuItem(title = self.config["gas"], callback = self.start_tracking)
        self.btc_button = rumps.MenuItem(title = self.config["btc"], callback = self.start_tracking)
        self.eth_button = rumps.MenuItem(title = self.config["eth"], callback = self.start_tracking)
        self.btcgas_button = rumps.MenuItem(title = self.config["btcgas"], callback = self.start_tracking)
        
        self.scrolling_button = rumps.MenuItem(title = self.config["scroll"], callback = self.scrolling)
        

        self.process_timer = rumps.Timer(self.on_tick, 1)
        self.process_timer.start()


        self.app.menu = [self.gas_button, self.eth_button, self.btcgas_button, self.btc_button, None, self.scrolling_button, None]

        self.app.icon = icon
        self.process_timer.count = 0

        self.start_tracking = False
        self.scrolling_bool = False

        self.get_data()

        self.start_tracking = True
    
    def get_data(self):

        if self.start_tracking:
            prev_gas = int(self.gas)
            prev_eth = float(self.ETH)
            prev_btc = float(self.BTC)
            prev_btcgas = float(self.btc_gas)
        
        
        self.gas, self.ETH, self.BTC, self.btc_gas = aggregate_data()

        if self.start_tracking:
            self.gas_grow = '🔻' if prev_gas > int(self.gas) else '🔺'
            self.eth_grow = '🔻' if prev_eth > float(self.ETH) else '🔺'
            self.btc_grow = '🔻' if prev_btc > float(self.BTC) else '🔺'
            self.gasbtc_grow = '🔻' if prev_btcgas > float(self.btc_gas) else '🔺'
        else:
            self.gas_grow, self.eth_grow, self.btc_grow, self.gasbtc_grow = '', '', '', ''

    def on_tick(self, sender):
        if sender.count == self.timeout:
            self.get_data()
            sender.count = 0

            self.setup_title()
        
        sender.count += 1

        if self.scrolling_bool and sender.count%10 == 0:

            self.flag = self.flags_list[self.i]
            self.setup_title()
            self.i += 1

            if self.i == len(self.flags_list):
                self.i = 0

    def setup_title(self):
        if self.flag == 'GAS':
            self.app.icon = ethgas
            self.app.title = f'Gas now: {self.gas} Gwei {self.gas_grow}'
        elif self.flag == 'ETH':
            self.app.icon = ethereum
            self.app.title = f'ETH now is {str(round(self.ETH, 2))}$ {self.eth_grow}'
        elif self.flag == 'BTCGAS':
            self.app.icon = btcgas
            self.app.title = f'BTC Gas: {self.btc_gas} sat/vB {self.btc_grow}'
        elif self.flag == 'BTC':
            self.app.icon = bitcoin
            self.app.title = f'BTC now is {self.BTC}$ {self.gasbtc_grow}'

    def start_tracking(self, sender):
        self.app.icon = None
        if sender.title == self.config["gas"]:
            self.flag = 'GAS'
            self.app.icon = ethgas
            self.app.title = f'Gas now: {self.gas} Gwei {self.gas_grow}'
        elif sender.title == self.config["btcgas"]:
            self.flag = 'BTCGAS'
            self.app.icon = btcgas
            self.app.title = f'BTC Gas: {self.btc_gas} sat/vB {self.btc_grow}'
        elif sender.title == self.config["btc"]:
            self.flag = 'BTC'
            self.app.icon = bitcoin
            self.app.title = f'BTC now is {self.BTC}$ {self.gasbtc_grow}'
        elif sender.title == self.config["eth"]:
            self.flag = 'ETH'
            self.app.icon = ethereum
            self.app.title = f'ETH now is {str(round(self.ETH, 2))}$ {self.eth_grow}'

    def scrolling(self, sender):
        sender.state = not sender.state
        self.scrolling_bool = not self.scrolling_bool

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = TrackerApp()
    app.run()