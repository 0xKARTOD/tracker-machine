import rumps

from tracker import *


class TrackerApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Tracker",
            "gas": "Show ETH Gas",
            "eth": "Show ETH price",
            "btc": "Show BTC price",
            "btcgas": "Show BTC Gas",
            "break_message": "Gas is high"
        }
        self.timeout = 60
        self.app = rumps.App(self.config["app_name"])
        self.gas_button = rumps.MenuItem(title = self.config["gas"], callback = self.start_gas_tracking)
        self.btc_button = rumps.MenuItem(title = self.config["btc"], callback = self.start_btc_tracking)
        self.eth_button = rumps.MenuItem(title = self.config["eth"], callback = self.start_eth_tracking)
        self.btcgas_button = rumps.MenuItem(title = self.config["btcgas"], callback = self.start_btcgas_tracking)
        

        self.process_timer = rumps.Timer(self.on_tick, 1)
        self.process_timer.start()


        self.app.menu = [self.gas_button, self.eth_button, self.btcgas_button, self.btc_button]

        self.set_up_menu()

    def set_up_menu(self):

        self.app.icon = 'icon.jpg'
        self.process_timer.count = 0

        self.start_tracking = False

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

            if self.flag == 'GAS':
                self.app.title = f'⛽ Gas now: {self.gas} Gwei {self.gas_grow}'
            elif self.flag == 'ETH':
                self.app.title = f'♢ETH now is {str(round(self.ETH, 2))}$ {self.eth_grow}'
            elif self.flag == 'BTCGAS':
                self.app.title = f'⛽ BTC Gas: {self.btc_gas} sat/vB {self.btc_grow}'
            elif self.flag == 'BTC':
                self.app.title = f'₿ now is {self.BTC}$ {self.gasbtc_grow}'
            
        sender.count += 1

    def start_gas_tracking(self, sender):
        self.app.icon = None
        self.flag = 'GAS'
        self.app.title = f'⛽ Gas now: {self.gas} Gwei {self.gas_grow}'
    def start_btcgas_tracking(self, sender):
        self.app.icon = None
        self.flag = 'BTCGAS'
        self.app.title = f'⛽ BTC Gas: {self.btc_gas} sat/vB {self.btc_grow}'
    def start_btc_tracking(self, sender):
        self.app.icon = None
        self.flag = 'BTC'
        self.app.title = f'₿ now is {self.BTC}$ {self.gasbtc_grow}'
    def start_eth_tracking(self, sender):
        self.app.icon = None
        self.flag = 'ETH'
        self.app.title = f'♢ETH now is {self.ETH}$ {self.eth_grow}'


    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = TrackerApp()
    app.run()