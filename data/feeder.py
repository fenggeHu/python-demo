import datetime
import requests
import pandas as pd
import eastmoney as em


class DataFeeder:
    def get(self, dataname: str, start=None, end=None):
        pass

    def store(self, dataname: str):
        pass


class RemoteDataFeeder(DataFeeder):
    def get(self, dataname: str, start=None, end=None):
        json = em.cn_chartbar(dataname, start, end)
        klines = json['data']['klines']
        df = pd.DataFrame(klines, columns=['date','open','close','high','low','volume','turnover','amplitude','chg_pct','chg','turnover_rate'])
        return df
