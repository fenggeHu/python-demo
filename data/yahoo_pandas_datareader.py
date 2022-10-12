from pandas_datareader import data as pdr

import yfinance as yf

# 通过yfinance下载
yf.pdr_override()  # <== that's all it takes :-)

# 作者说这种方式加载数据较快
# download dataframe
data = pdr.get_data_yahoo("AAPL", start="2021-01-01", end="2022-10-30")

print(data)
