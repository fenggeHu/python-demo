import random
import string
import requests

cb_str = "IO.XSRV2.CallbackList['{rds}']"
quotes_url = "http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList['{rds}']"


#
def volumeRise():
    return volumeRise(quotes_url + "/StatisticsService.getVolumeRiseConList?page=1&num=200&sort=changes_con&asc=0&node=adr_hk")


# Request & to json
def volumeRise(url):
    rds = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    dts = requests.get(url.format(rds=rds)).text
    callback = cb_str.format(rds=rds)
    start = dts.find(callback)
    json = ''
    if start > 0:
        json = dts[start + len(callback) + 1: len(dts) - 2]
    return json

# min line
min_url = "https://quotes.sina.cn/cn/api/openapi.php/CN_MinlineService.getMinlineData?symbol={symbol}&dpc=1"


def minline(symbol: str):
    json = requests.get(min_url.format(symbol=symbol)).text
    return json
