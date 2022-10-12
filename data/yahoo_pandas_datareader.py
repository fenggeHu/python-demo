from pandas_datareader import data as pdr

import yfinance as yf

yf.pdr_override()  # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("AAPL", start="2021-01-01", end="2022-10-30")

print(data)
