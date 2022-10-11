# %%
import backtrader as bt
import pandas as pd
import datetime

# dir
path = '/Users/max/.tibet/cn/features/'

# read csv data
# pd.read_csv(data, index_col='年份') # 指定列名
# pd.read_csv(data, index_col=['a','b']) # 多个索引
# pd.read_csv(data, index_col=[0, 3]) # 按列索引指定多个索引

symbol = 'SZ300760'
ohlcv = pd.read_csv(path + symbol + "/day.csv", index_col='datetime').loc['2022-01-01':'2022-01-31']
print(ohlcv)
# %%

# 实例化 cerebro
# cerebro = bt.Cerebro()
