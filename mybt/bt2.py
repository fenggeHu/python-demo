import pandas as pd
import backtrader as bt
from pandas_datareader import data as pdr
import datetime
import myst

import yfinance as yf

# 通过yfinance下载
yf.pdr_override()  # <== that's all it takes :-)

cerebro = bt.Cerebro()

symbol = 'MSFT'
dataframe = pdr.get_data_yahoo(symbol, start="2019-01-01")
# st_date = datetime.datetime(2021, 1, 1)
# ed_date = datetime.datetime(2022, 10, 15)
# datafeed = bt.feeds.PandasData(dataname=dataframe, fromdate=st_date, todate=ed_date)
cerebro.adddata(dataframe, name=symbol)
cerebro.addstrategy(myst.sma_strategy.SmaStrategy)

cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="SharpeRatio")
cerebro.addanalyzer(bt.analyzers.DrawDown, _name="DrawDown")

cerebro.broker.set_cash(100000.0)
cerebro.broker.setcommission(commission=0.0006)

cerebro.addsizer(bt.sizers.PercentSizer, percents=50)
result = cerebro.run()

print('SharpeRatio: ', result[0].analyzers.SharpRatio.get_analysis()['sharperatio'])
print('DrawDown: ', result[0].analyzers.DrawDown.get_analysis()['max']['drawdown'])
