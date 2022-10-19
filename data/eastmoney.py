# secid
import datetime
import requests


def gen_secid(symbol):
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
    if not start:
        start = "20100101"
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
          f'&fqt=0&beg={start}&end={end}'
    req = requests.get(url, timeout=30)  # request比pandas加载快
    json = req.json()
    return json


# symbol = "SH600010"
# dt = cn_chartbar(symbol, "2022-01-01")
# print(dt)
