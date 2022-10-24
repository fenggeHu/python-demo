import backtrader as bt

class Strategy1(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s: %s' % (dt.isoformat(), txt))

    def __init__(self) -> None:
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma5 = bt.ind.SMA(self.datas[0], period=5)
        self.rsi = bt.ind.RelativeStrengthIndex()

    def next(self):
        if self.order:
            return
        if self.dataclose > self.sma5:
            self.log('buy')
        if self.rsi > self.dataclose:
            self.log('sell')
