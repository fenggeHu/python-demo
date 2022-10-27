from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import talib
import pandas as pd
from datetime import datetime


class SmaCross(Strategy):
    def init(self):
        high, low, close = self.data.High, self.data.Low, self.data.Close
        self.ma1 = self.I(SMA, close, 5)
        self.ma2 = self.I(SMA, close, 10)
        # self.bbands = self.I(talib.BBANDS, close, 5, matype=talib.MA_Type.EMA)
        # # self.dema = self.I(talib.DEMA, price, 30)
        self.rsi = self.I(talib.RSI, close, timeperiod=14)
        # self.willr = self.I(talib.WILLR, high, low, close, timeperiod=14)

    def next(self):
        """ 从非空值的第2行开始迭代
            self下的所有_Indicator属性，取没有空值的最大行号，再next
            行号：最左是从0开始（从左到右0，1，2，...），最右是从-1开始（从右向左-1，-2，-3，...）
        """
        print(len(self.data.index), self.data.index[-1], float(self.data.Open), float(self.data.Close),
              self.data.Close[-2], self.data.Close[0])
        if self.data.Open >= self.data.Close:
            return
        if self.ma1 > self.data.Close:
            return
        if self.data.Close[-2] > self.data.Close:
            return

        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


# json = et.chartbar_json('SZ300760', '2022-01-01', '2022-10-25', 1)
# odf = et.to_df(json)
# data = odf.iloc[:, :5]  # 取前5列
odf = pd.read_csv("~/.tibet/cn/features/SZ300760/day.csv", index_col='datetime')
data = odf.loc['2022-01-01':'2022-10-30']
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']  # 对应的各列名
df = data.apply(pd.to_numeric)  # 各列数据必须是数字类型
df.index = df.index.map(lambda x: datetime.strptime(x, '%Y-%m-%d'))  # index必须是datetime
bt = Backtest(df, SmaCross, commission=.002, exclusive_orders=True)  # backtest实例化
stats = bt.run()  # 返回回测结果
print(stats)
bt.plot()  # 生成html图表展示
