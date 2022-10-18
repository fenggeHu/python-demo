# backtrader sample
import pandas as pd
import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.bband = bt.ind.BollingerBands()

    def next(self):
        pass
