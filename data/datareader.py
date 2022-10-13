import pandas_datareader as pdr

# 引入pandas_datareader的wb.py
from pandas_datareader import wb

# fred = pdr.get_data_fred('GS10')
# print(fred)

countries = wb.get_countries()
print(countries)

# countries = wb.WorldBankReader().get_countries()
# print(countries)
