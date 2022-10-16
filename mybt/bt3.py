import backtrader as bt
import pandas as pd
import datetime
from pandas_datareader import data as pdr
import yfinance as yf


class MyStrategy(bt.Strategy):
    def __init__(self):
        print('init')

    def start(self):
        print('start')

    def prenext(self):
        print('prenext')

    def next(self):
        print('next: ', self.datas[0].datetime.date(0), self.data.close[0], self.data.close[-1], self.data.close[-2])

    # def stop(self):
    #     print('stop')

    # def notify_cashvalue(self, cash, value):
    #     print('notify_cashvalue')
    #
    # def notify_fund(self, cash, value, fundvalue, shares):
    #     print('fund: cash %.2f, value %.2f, fundvalue %.2f, shares %.2f' % (cash, value, fundvalue, shares))
    #
    # def notify_order(self, order):
    #     print('notify_order', order)
    #
    # def notify_trade(self, trade):
    #     print('notify_trade', trade)
    #
    # def notify_store(self, msg, *args, **kwargs):
    #     print('notify_store: %s' % msg)
    #
    # def notify_data(self, data, status, *args, **kwargs):
    #     print('notify_data: ', data, status)
    #
    # def cancel(self, order):
    #     print('cancel', order)


cerebro = bt.Cerebro()

# html = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
# tickers = html[0].Symbol.to_list()
# tickers = [i.replace('.', '-') for i in tickers]
#
# df = yf.download(tickers[0], start='2011-01-01')
# st_date = datetime.datetime(2021, 1, 1)
# ed_date = datetime.datetime(2022, 10, 15)
# datafeed = bt.feeds.PandasData(dataname=df, fromdate='2022-01-01', todate='2022-10-14')

df = yf.download('AAPL', start='2022-10-01')
feed = bt.feeds.PandasData(dataname=df)

cerebro.adddata(feed)
cerebro.addstrategy(MyStrategy)
cerebro.run()
cerebro.plot()
