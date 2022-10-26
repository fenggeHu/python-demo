import pandas as pd
from datetime import datetime

from backtesting_py.btg1 import Btgs1
from data import eastmoney as et
from backtesting import Backtest


# run a symbol testing
def run(strategy, symbol, start=None, end=None, plot=False):
    json = et.chartbar_json(symbol, start, end, 1)
    odf = et.to_df(json)
    data = odf.iloc[:, :5]  # 取前5列
    data.columns = ['Open', 'Close', 'High', 'Low', 'Volume']  # eastmoney对应的各列名顺序
    df = data.apply(pd.to_numeric)  # 各列数据必须是数字类型
    df.index = df.index.map(lambda x: datetime.strptime(x, '%Y-%m-%d'))  # index必须是datetime
    bt = Backtest(df, strategy, commission=.002, exclusive_orders=True)  # backtest实例化
    stats = bt.run()  # 返回回测结果
    print(stats)
    if plot:
        bt.plot()  # 生成html图表展示


# HS300
tables = pd.read_html("https://en.wikipedia.org/wiki/CSI_300_Index")
csi300 = tables[3]
# 股票代码补齐6位 - int转str再填充0
csi300['Index'] = csi300['Index'].map(lambda x: str(x).zfill(6))
# # 设置Index列为索引
# csi300.set_index(['Index'], inplace=True)
for s in csi300['Index']:
    run(Btgs1, s, '2022-09-01')
