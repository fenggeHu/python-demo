# importing pandas
import pandas as pd
from pandas_datareader import data as pdr

import yfinance as yf

from data import local_csv_file
from data.feeder import DataFeeder


class LocalCsvFeeder(DataFeeder):
    def store(self):
        pass


# TODO 读写文件
symbol = "AAPL"
file = local_csv_file.format("us", symbol)
dl = pdr.get_data_yahoo(symbol, start="2021-01-01", end="2022-10-30")
local = pd.read_csv(file, index_col='datetime')

m1 = map(dl["datetime"], dl)
# merging two csv files
df = pd.concat([m1, local], ignore_index=True)

df.to_csv(path_or_buf=file)

print(df)
