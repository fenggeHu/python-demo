import random
import string
import requests

import pandas as pd

rds = ''.join(random.sample(string.ascii_letters + string.digits, 16))
dts = requests.get(
    f"http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['{rds}']"
    f"/StatisticsService.getSummaryMonthList?page=1&num=50&sort=amount&asc=1&node=adr_hk").text

callback = f"IO.XSRV2.CallbackList['{rds}']"
start = dts.find(callback)
json = ''
if start > 0:
    json = dts[start + len(callback) + 1: len(dts) - 2]

dt = pd.read_json(json)
print(dt)
