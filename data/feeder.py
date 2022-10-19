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
        dt = [s.split(',') for s in klines]
        ori_labels = ['date', 'open', 'close', 'high', 'low', 'volume', 'turnover', 'amplitude', 'chg_pct', 'chg',
                      'turnover_rate']
        df = pd.DataFrame.from_records(dt, columns=ori_labels, index='date')
        df['volume'] = df.volume.map(lambda x: f'{x}00')  # 手*100
        labels = ['open', 'high', 'low', 'close', 'volume', 'turnover', 'amplitude', 'chg_pct', 'chg', 'turnover_rate']
        df = df[labels]  # 调整一下column顺序
        return df
