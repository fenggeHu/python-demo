import random
import string
import requests

cb_str = "IO.XSRV2.CallbackList['{rds}']"
jsonp_v2 = "http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['{rds}']"


# 不含jsonp_v2
def jsonpV2(shorturl):
    return get(jsonp_v2 + shorturl)


# Request & to json
def get(url):
    rds = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    dts = requests.get(url.format(rds=rds)).text
    callback = cb_str.format(rds=rds)
    start = dts.find(callback)
    json = ''
    if start > 0:
        json = dts[start + len(callback) + 1: len(dts) - 2]
    return json
