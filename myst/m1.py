import pandas as pd
import backtrader as bt
from datetime import datetime
import yfinance as yf
from pandas_datareader import data as pdr

# 通过yfinance下载
yf.pdr_override()  # <== that's all it takes :-)
symbol = "AAPL"
df = pdr.get_data_yahoo(symbol, '2020-01-01', '2022-12-31')  # Set my column names
df.columns = ['high', 'low', 'open', 'close', 'volume', 'adj_close']
data = bt.feeds.PandasData(dataname=df)

ma5 = bt.ind.SMA(data, period=5)
ma5
