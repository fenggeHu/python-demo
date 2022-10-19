# from __future__ import (absolute_import, division, print_function,
#                         unicode_literals)
import backtrader as bt


class St(bt.Strategy):
    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(self.data)


data = bt.feeds.BacktraderCSVData(dataname='/Users/max/sz000001.csv')
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(St)
cerebro.run()
cerebro.plot(style='bar')
