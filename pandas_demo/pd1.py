# %%
from numbers import Number

import pandas as pd
from data import local_data_path

from typing import Sequence

# read csv data
# pd.read_csv(data, index_col='年份') # 指定列名
# pd.read_csv(data, index_col=['a','b']) # 多个索引
# pd.read_csv(data, index_col=[0, 3]) # 按列索引指定多个索引


symbol = 'SZ300760'
ohlcv = pd.read_csv(local_data_path + symbol + "/day.csv", index_col='datetime').loc['2022-09-01':'2022-09-30']
ohlcv.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
print(ohlcv)


# %%
def gets(series1: Sequence):
    return (
        series1.values if isinstance(series1, pd.Series) else
        (series1, series1) if isinstance(series1, Number) else
        series1)


series = gets(ohlcv)
print(series)
