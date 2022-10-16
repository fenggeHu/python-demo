import backtrader as bt
import pandas as pd
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
        print('next')

    def stop(self):
        print('stop')

    def notify_cashvalue(self, cash, value):
        print('notify_cashvalue')

    def notify_fund(self, cash, value, fundvalue, shares):
        print('fund: cash %.2f, value %.2f, fundvalue %.2f, shares %.2f' % (cash, value, fundvalue, shares))

    def notify_order(self, order):
        print('notify_order', order)

    def notify_trade(self, trade):
        print('notify_trade', trade)

    def notify_store(self, msg, *args, **kwargs):
        print('notify_store: %s' % msg)

    def notify_data(self, data, status, *args, **kwargs):
        print('notify_data: ', data, status)

    def cancel(self, order):
        print('cancel', order)


cerebro = bt.Cerebro()

html = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
tickers = html[0].Symbol.to_list()
tickers = [i.replace('.', '-') for i in tickers]


cerebro.adddata()
