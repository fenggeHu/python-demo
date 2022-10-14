# %%
import pandas as pd
import backtrader as bt
import datetime

import mybt.s1
from data import local_data_path

# read csv data
# pd.read_csv(data, index_col='年份') # 指定列名
# pd.read_csv(data, index_col=['a','b']) # 多个索引
# pd.read_csv(data, index_col=[0, 3]) # 按列索引指定多个索引

symbol = 'SZ300760'
ohlcv = pd.read_csv(local_data_path + symbol + "/day.csv", index_col='datetime',
                    parse_dates=['datetime'])  ##.loc['2022-01-01':'2022-01-31']
print(ohlcv)
# %%
st_date = datetime.datetime(2021, 1, 1)
ed_date = datetime.datetime(2022, 10, 15)
datafeed = bt.feeds.PandasData(dataname=ohlcv, fromdate=st_date, todate=ed_date)
# 实例化 cerebro
cerebro = bt.Cerebro()
cerebro.adddata(datafeed, name=symbol)
# print(f"{symbol} data loaded")
# %%
# 初始资金
cerebro.broker.setcash(200000.0)
# 佣金
cerebro.broker.setcommission(commission=0.0003)
# 滑点
cerebro.broker.set_slippage_perc(perc=0.005)
cerebro.addanalyzer(bt.analyzers.TimeReturn, _name='pnl')  # 返回收益率时序数据
cerebro.addanalyzer(bt.analyzers.AnnualReturn, _name='_AnnualReturn')  # 年化收益率
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')  # 夏普比率
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')  # 回撤

# %%
# 添加策略 TODO 写策略
cerebro.addstrategy(mybt.s1.MyStrategy)

# %%
# 启动回测
result = cerebro.run()
# 从返回的 result 中提取回测结果
strat = result[0]
# 返回日度收益率序列
daily_return = pd.Series(strat.analyzers.pnl.get_analysis())
# 打印评价指标
print("--------------- AnnualReturn -----------------")
print(strat.analyzers._AnnualReturn.get_analysis())
print("--------------- SharpeRatio -----------------")
print(strat.analyzers._SharpeRatio.get_analysis())
print("--------------- DrawDown -----------------")
print(strat.analyzers._DrawDown.get_analysis())
