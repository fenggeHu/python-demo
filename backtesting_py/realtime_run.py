import pandas as pd
from datetime import datetime

from backtesting_py.btg1 import Btgs
from data import eastmoney as et
from backtesting import Backtest

# 显示所有行和列
pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#
today = str(datetime.today().date())
cash = 100_000  # 初始资金


# run a symbol testing
def run(strategy, symbol, start=None, end=None, plot=False):
    json = et.chartbar_json(symbol, start, end, 1)
    odf = et.to_df(json)
    if len(odf) == 0 or odf.index[len(odf) - 1] != today:
        print(f'No data: {symbol}')
        return
    print(f'{symbol} is running')
    data = odf[['open', 'high', 'low', 'close', 'turnover']]  # 取前5列
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']  # eastmoney对应的各列名顺序
    df = data.apply(pd.to_numeric)  # 各列数据必须是数字类型
    df.index = df.index.map(lambda x: datetime.strptime(x, '%Y-%m-%d'))  # index必须是datetime
    bt = Backtest(df, strategy, cash=cash, commission=.002, exclusive_orders=True)  # backtest实例化
    stats = bt.run()  # 返回回测结果
    # print(stats['_trades'])  # https://kernc.github.io/backtesting.py/doc/examples/Quick%20Start%20User%20Guide.html
    if plot and stats['Equity Final [$]'] != cash:  # 不知道怎么判断有买卖了，金额变化了
        bt.plot(filename=symbol)  # 生成html图表展示


# run(Btgs1, 'SZ300760', "2022-01-01", "2022-01-31", plot=True)

# HS300
tables = pd.read_html("https://en.wikipedia.org/wiki/CSI_300_Index")
csi300 = tables[3]
# 股票代码补齐6位 - int转str再填充0
csi300['Index'] = csi300['Index'].map(lambda x: str(x).zfill(6))
# # 设置Index列为索引
# csi300.set_index(['Index'], inplace=True)
for s in csi300['Index']:
    run(Btgs, s, '2022-08-01', plot=True)

print(f'finished')
