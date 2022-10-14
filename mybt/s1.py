import backtrader as bt
import backtrader.indicators as btind


class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = btind.SimpleMovingAverage(period=15)

    def next(self):
        print(self.sma)
        print(self.data.close)
        if self.sma > self.data.close:
            # Do something

            pass

        elif self.sma < self.data.close:
            # Do something else
            pass

