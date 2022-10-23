import pandas as pd

table = pd.read_html("https://en.wikipedia.org/wiki/CSI_300_Index")
csi300 = table[3]
# 股票代码补齐6位 - int转str再填充0
csi300['Index'] = csi300['Index'].map(lambda x: str(x).zfill(6))
# 设置Index列为索引
csi300.set_index(['Index'], inplace=True)
