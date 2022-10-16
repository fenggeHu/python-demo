import backtrader as bt


class SmaStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.data0.close
        self.order = None
        self.buyprice = None
        self.buycomm = None

        self.sma = bt.ind.SimpleMovingAverage(self.data0, period=15)

    def next(self):
        if not self.position:
            if self.dataclose[0] > self.sma[0]:
                self.buy()
        elif self.dataclose[0] < self.sma[0]:
            self.close()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY executed, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
            else:
                self.log(
                    'SELL executed, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log('Operation Profit, Gross %.2f, Net %.2f' %
                 (trade.pnl, trade.pnlcomm))

    def log(self, txt, dt=None, doprint=False):
        if doprint:
            print('%s, %s' % (dt.isoformat(), txt))
           