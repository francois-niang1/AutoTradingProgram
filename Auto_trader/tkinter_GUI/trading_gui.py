#interface graphique
import tkinter as tk
from threading import Thread
from main import main
from strategies.mean_reversion.mean_reversion import SimpleStrategy
from utils.api_utils import BinanceClient

class TradingApp:
    def __init__(self, master):
        self.master = master
        master.title("Trading App")

        self.start_button = tk.Button(master, text="Start Trading", command=self.start_trading)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Trading", command=self.stop_trading)
        self.stop_button.pack()

        self.status_label = tk.Label(master, text="Status: Idle")
        self.status_label.pack()

        self.trading_thread = None
        self.binance_client = BinanceClient()
        self.strategy = SimpleStrategy(self.binance_client)

    def start_trading(self):
        self.status_label.config(text="Status: Trading")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.trading_thread = Thread(target=main)
        self.trading_thread.start()

    def stop_trading(self):
        self.status_label.config(text="Status: Idle")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        if self.trading_thread:
            self.trading_thread.join()

def run_gui():
    root = tk.Tk()
    app = TradingApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()