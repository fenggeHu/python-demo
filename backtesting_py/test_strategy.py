from backtesting import Backtest
from btg import Btgs
# 找不到module
import sys

sys.path.append('/Users/max/mypython/python-demo')
from data import eastmoney

lines = eastmoney.cn_chartbar('SH000001', start='2022-01-01')
df = eastmoney.to_df2(lines)

# import pandas as pd
# df.index = pd.to_datetime(df.index)
bt = Backtest(df, Btgs, commission=.002, exclusive_orders=True)
stats = bt.run()
bt.plot()
