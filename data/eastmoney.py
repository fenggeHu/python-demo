# secid
import datetime
import requests
import pandas as pd


def gen_secid(symbol):
    if len(symbol) == 6:
        if symbol[0] == '6':
            symbol = 'SH' + symbol
        elif symbol[0] == '3' or symbol[0] == '0':
            symbol = 'SZ' + symbol
        else:
            raise RuntimeError(f'Symbol Err: {symbol}')
    elif len(symbol) != 8:
        raise RuntimeError(f'Symbol Err: {symbol}')

    exchange = symbol[0:2]
    code = symbol[2:]
    if exchange == "SH":
        return f"1.{code}"
    elif exchange == "ZS":
        f3 = code[0:3]
        if f3 == "000":
            return f"1.{code}"

    return f"0.{code}"

# 不复权
def cn_chartbar(dataname: str, start: str = None, end: str = None):
    return chartbar_json(dataname, start, end, 0)


# json转pandas dataframe
def to_df(json):
    klines = json['data']['klines']
    dt = [s.split(',') for s in klines]
    ori_labels = ['date', 'open', 'close', 'high', 'low', 'volume',
                  'turnover', 'amplitude', 'chg_pct', 'chg', 'turnover_rate']
    df = pd.DataFrame.from_records(dt, columns=ori_labels, index='date')
    df = df.apply(pd.to_numeric)
    return df

# 用于strategy的列
def to_df2(json):
    df = to_df(json)
    df = df[['open','high','low','close','turnover']] # 只需要这几列
    df.columns = ['open','high','low','close','volume'] # turnover-->volume
    return df

#
def chartbar_json(dataname: str, start: str = None, end: str = None, adj=0):
    if not start:
        start = "20200101"
    else:
        start = start.replace("-", "")
    if not end:
        end = datetime.datetime.now().strftime("%Y%m%d")
    else:
        end = end.replace("-", "")
    secid = gen_secid(dataname)
    # 不复权 : 0; 前复权 : 1; 后复权 : 2
    url = f'https://push2his.eastmoney.com/api/qt/stock/kline/get?secid={secid}&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5' \
          f'&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58%2Cf59%2Cf60%2Cf61&klt=101' \
          f'&fqt={adj}&beg={start}&end={end}'
    req = requests.get(url, timeout=30)  # request比pandas加载快
    json = req.json()
    return json

# json = chartbar_json('SZ300760', '2020-01-01', '2022-10-25', 1)
# df = to_df(json)
# df = df.iloc[:, :5]
# print(df)
