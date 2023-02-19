import requests
import json

csindex_url = "https://www.csindex.com.cn/csindex-home/indexInfo/security-industry-search"


def cnSecurityIndustry():
    page = 1
    payload = {
        "pageNum": page,
        "pageSize": 40,
        "searchInput": ""
    }
    ret = []
    response = requests.post(csindex_url, json=payload)
    if response.status_code != 200:
        return ret
    js = json.loads(response.text)
    ret.extend(js['data'])
    print('Page Count: ', js['size'])
    while page + 1 < js['size']:
        page += 1
        payload["pageNum"] = page
        # print('load page: ',page)
        response = requests.post(csindex_url, json=payload)
        js = json.loads(response.text)
        ret.extend(js['data'])
    # python的filter返回的是一个Iterator惰性序列，需要用list()函数获得结果
    return list(filter(lambda x: x['securityCode'].count(".HK") == 0, ret))


# cnSecurityIndustry()
