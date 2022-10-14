import backtrader as bt
import backtrader.indicators as btind


class MyStrategy(bt.Strategy):
    def __init__(self):
        self.sma = btind.SimpleMovingAverage(period=15)

    def log(self, txt):
        dt = self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        print(self.sma)
        print(self.data.close)
        self.log('Close, %.2f' % self.data.close[0])
        if self.sma > self.data.close:
            # Do something

            pass

        elif self.sma < self.data.close:
            # Do something else
            pass

