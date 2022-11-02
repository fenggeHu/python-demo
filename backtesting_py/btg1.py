import backtesting as bt
from backtesting.lib import crossover
import datetime
import talib


class Btgs1(bt.Strategy):
    def init(self):
        self.today = str(datetime.date.today())
        close = self.data.Close
        self.ma5 = self.I(talib.SMA, close, 5)
        self.ma10 = self.I(talib.SMA, close, 10)
        self.ma20 = self.I(talib.SMA, close, 20)

    def next(self):
        # 只判断当天
        if str(self.data.index[-1])[0:10] < self.today:
            return

        if self.data.High[-1] == self.data.Open[-1] and self.data.Close[-1] == self.data.Open[-1]:
            return
        if self.data.Volume[-1] < 30000:
            return
        if (self.data.High[-1] != self.data.Open[-1]) and (self.data.Close[-1] - self.data.Open[-1]) / (self.data.High[-1] - self.data.Open[-1]) < 0.3:
            return
        if (self.ma5[-1] - self.ma10[-1]) / self.ma5[-1] < -0.01 or (self.ma5[-1] - self.ma20[-1]) / self.ma5[-1] < -0.01:
            return
        if self.data.Close[-1] < self.data.Open[-1] or self.data.Close[-1] < self.data.Close[-2]:
            return
        if (self.data.High[-1] - self.data.Close[-1]) / self.data.Close[-1] > 0.04:
            return
        if self.ma5[-1] < self.ma5[-2] or self.ma5[-1] < self.ma5[-3]:
            return
        if self.data.Close[-1] < self.hisMinPrice():
            return

        if crossover(self.ma5, self.ma10):
            self.buy()
        elif crossover(self.ma10, self.ma5):
            self.sell()

    def hisMinPrice(self, n=20):
        """ get history min close"""
        size = min(len(self.data.Close), n)
        price = 100000000.00
        for i in range(1, size):
            price = min(price, self.data.Close[- i])
        return price
