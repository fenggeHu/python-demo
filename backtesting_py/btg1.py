import backtesting as bt
import talib


class Btgs1(bt.Strategy):
    def init(self):
        close = self.data.Close
        self.ma5 = self.I(talib.SMA, close, 5)

    def next(self):
        if self.data.Close > self.data.Open and self.data.Close > self.data.Close[-2]:
            if self.position.size > 0:
                self.buy(limit=200)
            else:
                self.buy(size=0.5, limit=100)

        elif self.data.Close < self.ma5:
            self.sell()

        # if self.data.Open >= self.data.Close:
        #     return
        # if self.ma5 > self.data.Close:
        #     return
        # if self.data.Close[-2] > self.data.Close:
        #     return
