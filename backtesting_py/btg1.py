from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import talib
from data import eastmoney as et
import pandas as pd
from datetime import datetime


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma10 = self.I(SMA, price, 10)
        self.ma20 = self.I(SMA, price, 20)
        self.ma30 = self.I(talib.SMA, price, 30)

    def next(self):
        if crossover(self.ma10, self.ma30):
            self.buy()
        elif crossover(self.ma20, self.ma10):
            self.sell()


json = et.chartbar_json('SZ300760', '2020-01-01', '2022-10-25', 1)
odf = et.to_df(json)
data = odf.iloc[:, :5]  # 取钱5列
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df = data.apply(pd.to_numeric)
df.index = df.index.map(lambda x: datetime.strptime(x, '%Y-%m-%d'))
bt = Backtest(df, SmaCross, commission=.002, exclusive_orders=True)
stats = bt.run()
bt.plot()
