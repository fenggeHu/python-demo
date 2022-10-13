import pandas as pd

# read_html 找到html内的所有table，得到数组。 - 找不到table就会抛异常
# https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
html = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
tickers = html[0].Symbol.to_list()
tickers = [i.replace('.', '-') for i in tickers]

html = pd.read_html("https://www.moneydj.com/us/rank/rank0009")
tickers = html[1]["代碼"].to_list()
print(tickers)

# read json
json = pd.read_json("https://www.moneydj.com/us/rest/list0003a2/DJI")
print(json)
