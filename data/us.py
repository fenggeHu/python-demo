# 使用datareader从yahoo finance下载数据
import os
from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
# 通过yfinance下载
yf.pdr_override()  # <== that's all it takes :-)

def download(sym, start, end):
    data = pdr.get_data_yahoo(sym, start, end)
    filepath = f'{root}/{region}/features/{sym}'
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    filename = f'{filepath}/day.csv'
    print(f'{sym} to file: {filename}')
    data.to_csv(filename)


root = "/Users/max/.tibet"
region = "us"

# apple_info = pd.read_html('https://www.moneydj.com/us/basic/basic0001/AAPL')
# gspc = pd.read_json('https://www.moneydj.com/us/rest/list0003a2/GSPC')
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
tickers = sp500[0].Symbol
tickers = [i.replace('.', '-') for i in tickers]

# 数据下载
# for i in range(len(tickers)):
#     download(tickers[i], '2010-01-01', '2022-12-31')

symbol = 'MMM'
df = pd.read_csv(f'{root}/{region}/features/{symbol}/day.csv')
print()
